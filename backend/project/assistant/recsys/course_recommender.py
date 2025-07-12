# assistant/recsys/course_recommender.py
import numpy as np
from django.db.models import QuerySet
from ..models import Course

W = {                      # weight scheme
    "skill":   0.5,
    "level":   0.2,
    "domain":  0.1,
    "goal":    0.1,
    "rating":  0.1,
}

def _level_match(course_level, user_exp):
    # Simple mapping
    table = {
        ("Beginner", "Beginner"): 1.0,
        ("Beginner", "Intermediate"): 0.8,
        ("Intermediate", "Intermediate"): 1.0,
        ("Intermediate", "Beginner"): 0.6,
        ("Advanced", "Expert"): 1.0,
    }
    return table.get((course_level, user_exp), 0.5)

def compute_score(course, student_profile) -> float:
    """
    student_profile: dict with keys
        skills_wanted, experience_level, domain_interest, learning_goal
    """
    skill_overlap = len(set(course.skills_taught)
                        & set(student_profile["skills_wanted"]))
    skill_match = skill_overlap / max(1, len(student_profile["skills_wanted"]))

    score = (
        skill_match                                * W["skill"] +
        _level_match(course.level,
                     student_profile["experience_level"]) * W["level"] +
        (1.0 if course.domain == student_profile["domain_interest"] else 0.0)
                                                   * W["domain"] +
        (1.0 if student_profile["learning_goal"] in course.description
             else 0.0)                             * W["goal"] +
        (course.rating / 5.0)                      * W["rating"]
    )
    return round(score, 3)

def recommend(student_profile: dict,
              top_k: int = 10,
              catalogue: QuerySet = None):
    """
    Returns top‑k Course objects sorted by score.
    """
    catalogue = catalogue or Course.objects.all()
    scored = [(compute_score(c, student_profile), c) for c in catalogue]
    scored.sort(reverse=True, key=lambda t: t[0])
    return [c for _, c in scored[:top_k]]
