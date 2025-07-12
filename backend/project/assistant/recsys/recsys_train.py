import pandas as pd
import numpy as np
import json
import itertools
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import HistGradientBoostingRegressor
import joblib

############################################################
# 1. Load the synthetic data
############################################################
df = pd.read_csv("student_data_1000.csv")

# Make list‑columns actual Python lists
df["skills_offered"] = df["skills_offered"].apply(json.loads)
df["skills_wanted"] = df["skills_wanted"].apply(json.loads)
df["tech_stack_familiarity"] = df["tech_stack_familiarity"].apply(json.loads)

############################################################
# 2. Create (searcher, candidate) pairs
#    – In an actual system you’d use real logs; here we brute‑force small sample
############################################################
pairs = []
for i, j in itertools.combinations(df.index, 2):
    searcher = df.loc[i]
    candidate = df.loc[j]

    # Symmetric pairs so model can generalise
    for a, b in [(searcher, candidate), (candidate, searcher)]:
        pairs.append({
            "searcher_id": a.name,
            "candidate_id": b.name,
            "skill_match_score": len(set(a["skills_wanted"]).intersection(b["skills_offered"]))
                                / max(1, len(a["skills_wanted"])),
            "availability_score": 1.0 if a["availability_days"] == b["availability_days"] else 0.5,
            "reliability_score": b["reliability_score"] if not np.isnan(b["reliability_score"]) else 0.5,
            "experience_compatibility_score": 1.0 if a["experience_level"] == b["experience_level"] else 0.6,
            "rating_score": b["average_rating"] / 5,
            "college_or_place_match": 1.0 if a["college_name"] == b["college_name"]
                                          or a["place"] == b["place"] else 0.0,
            "recent_activity_score": b["response_rate"],          # proxy for “active user”
            "profile_completeness": (
                len(b["skills_offered"]) + len(b["skills_wanted"])
            ) / 10.0                                              # crude completeness metric
        })

pairs_df = pd.DataFrame(pairs)

############################################################
# 3. Compute the target “score” using your weight formula
############################################################
w = dict(skill_match=0.4, availability=0.2, reliability=0.1,
         experience=0.1, rating=0.05, college_place=0.05,
         recent=0.05, completeness=0.05)

pairs_df["target_score"] = (
      pairs_df["skill_match_score"]      * w["skill_match"]
    + pairs_df["availability_score"]     * w["availability"]
    + pairs_df["reliability_score"].fillna(0.5) * w["reliability"]
    + pairs_df["experience_compatibility_score"] * w["experience"]
    + pairs_df["rating_score"]           * w["rating"]
    + pairs_df["college_or_place_match"] * w["college_place"]
    + pairs_df["recent_activity_score"]  * w["recent"]
    + pairs_df["profile_completeness"]   * w["completeness"]
)

# Features used for learning (numeric only for simplicity)
feature_cols = [
    "skill_match_score", "availability_score", "reliability_score",
    "experience_compatibility_score", "rating_score",
    "college_or_place_match", "recent_activity_score",
    "profile_completeness"
]
X = pairs_df[feature_cols]
y = pairs_df["target_score"]

############################################################
# 4. Train a regressor (fast & interpretable)
############################################################
model = HistGradientBoostingRegressor(max_depth=4, learning_rate=0.1,
                                      max_iter=200, l2_regularization=0.01,
                                      early_stopping=True)
model.fit(X, y)

print("Training RMSE:",
      mean_squared_error(y, model.predict(X), squared=False))

############################################################
# 5. Persist the model
############################################################
joblib.dump(model, "profile_ranker.joblib")
print("Saved model to profile_ranker.joblib")
