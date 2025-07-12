import json, joblib, os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chat import get_chat_response
from .recsys.rank_profiles import rank_candidates
from django.contrib.auth.decorators import login_required
from .recsys.course_recommender import recommend
from .models import Course
from core_app.models import Profile
from .models import SwapRequest
import json

MODEL_PATH = os.path.join(os.path.dirname(__file__),
                          "recsys/profile_ranker.joblib")
ranker = joblib.load(MODEL_PATH)

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
def split_skills(skills_str: str):
    """Convert comma‑separated 'Photoshop, Excel' → ['Photoshop','Excel']"""
    return [s.strip() for s in skills_str.split(",") if s.strip()]


# ------------------------------------------------------------------
# 1) Public profile list   GET /api/public_profiles/
# ------------------------------------------------------------------
@require_GET
def public_profiles(request):
    q       = request.GET.get("q", "").lower()
    avail   = request.GET.get("availability", "")
    qs = Profile.objects.filter(public=True)
    if q:
        qs = qs.filter(skills__icontains=q)
    if avail:
        qs = qs.filter(availability__iexact=avail)

    data = [
        {
            "id": p.id,
            "name": p.name or p.user.username,
            "location": p.location,
            "skills_offered": split_skills(p.skills),
            # With the simple Profile model we don't track wanted‑skills yet
            "skills_wanted": [],
            "rating": getattr(p, "average_rating", 0.0),
            "photo_url": "/static/img/default.jpg",   # change if you store avatars
        }
        for p in qs
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        text = json.loads(request.body).get("message", "")
        return JsonResponse({"response": get_chat_response(text)})
    return JsonResponse({"error": "POST only"}, status=405)

# ------------------------------------------------------------------
# 2) Course recommendations   GET /api/courses/
# ------------------------------------------------------------------
@login_required
@require_GET
def courses_api(request):
    """
    Returns top‑k course suggestions based on a *minimal* profile.
    """
    profile = request.user.profile                    # OneToOne link
    query_want = request.GET.get("want", "")
    student_dict = {
        "skills_wanted": split_skills(query_want) or split_skills(profile.skills),
        # The following keys are required by course_recommender but are
        # NOT stored in the simple Profile model, so we pass safe defaults.
        "experience_level": "Beginner",
        "domain_interest":  "",
        "learning_goal":    "",
    }

    top_k = int(request.GET.get("top_k", 10))        # <-- only once!
    courses = recommend(student_dict, top_k=top_k)

    return JsonResponse(
        [
            {
                "title":  c.title,
                "url":    c.url,
                "skills": c.skills_taught,
                "level":  c.level,
                "rating": c.rating,
            }
            for c in courses
        ],
        safe=False,
    )


# ------------------------------------------------------------------
# 3) Swap creation   POST /api/create_swap/
# ------------------------------------------------------------------
@csrf_exempt
@require_POST
def create_swap(request):
    payload = json.loads(request.body)
    # You said you hadn't added SwapRequest yet; stub success response:
    return JsonResponse({"ok": True})


# ------------------------------------------------------------------
# 4) Chat endpoint (unchanged)
# ------------------------------------------------------------------
@csrf_exempt
@require_POST
def chat_api(request):
    text = json.loads(request.body).get("message", "")
    reply = get_chat_response(text)
    return JsonResponse({"response": reply})


