import joblib
import pathlib
import pandas as pd
import json
import numpy as np

MODEL_PATH = pathlib.Path(__file__).resolve().parent / "profile_ranker.joblib"
ranker = joblib.load(MODEL_PATH)
students = pd.read_csv("student_data_1000.csv")
students["skills_offered"] = students["skills_offered"].apply(json.loads)
students["skills_wanted"] = students["skills_wanted"].apply(json.loads)

def rank_candidates(searcher_id, top_k=10):
    a = students.loc[searcher_id]
    feature_rows = []
    candidate_ids = []

    for idx, b in students.iterrows():
        if idx == searcher_id:
            continue
        candidate_ids.append(idx)
        feature_rows.append([
            len(set(a["skills_wanted"]).intersection(b["skills_offered"]))
                / max(1, len(a["skills_wanted"])),
            1.0 if a["availability_days"] == b["availability_days"] else 0.5,
            b["reliability_score"] if not np.isnan(b["reliability_score"]) else 0.5,
            1.0 if a["experience_level"] == b["experience_level"] else 0.6,
            b["average_rating"] / 5,
            1.0 if a["college_name"] == b["college_name"]
                  or a["place"] == b["place"] else 0.0,
            b["response_rate"],
            (len(b["skills_offered"]) + len(b["skills_wanted"])) / 10.0
        ])

    preds = ranker.predict(pd.DataFrame(feature_rows,
                        columns=["skill_match_score","availability_score","reliability_score",
                                 "experience_compatibility_score","rating_score",
                                 "college_or_place_match","recent_activity_score",
                                 "profile_completeness"]))

    top_indices = np.argsort(-preds)[:top_k]
    return students.iloc[[candidate_ids[i] for i in top_indices]]

# Example:
if __name__ == "__main__":
    ranked = rank_candidates(searcher_id=0, top_k=5)
    print(ranked[["student_name", "skills_offered", "average_rating"]])
