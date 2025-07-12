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

MODEL_PATH = os.path.join(os.path.dirname(__file__),
                          "recsys/profile_ranker.joblib")
ranker = joblib.load(MODEL_PATH)

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        text = json.loads(request.body).get("message", "")
        return JsonResponse({"response": get_chat_response(text)})
    return JsonResponse({"error": "POST only"}, status=405)

@csrf_exempt
def recommendations_api(request):
    if request.method == "GET":
        searcher_id = int(request.GET.get("searcher_id"))
        results = rank_candidates(searcher_id, ranker, top_k=10)
        return JsonResponse(results.to_dict(orient="records"), safe=False)
    return JsonResponse({"error": "GET only"}, status=405)

@login_required
def courses_api(request):
    """
    GET /api/courses/?top_k=5
    """
    user = request.user
    profile = StudentProfile.objects.get(user=user)
    student_dict = {
        "skills_wanted": profile.skills_wanted,          # List[str]
        "experience_level": profile.experience_level,    # Beginner / Intermediate / Expert
        "domain_interest": profile.domain_interest,      # Software / Design / Business
        "learning_goal": profile.learning_goal,          # str
    }
    top_k = int(request.GET.get("top_k", 10))
    courses = recommend(student_dict, top_k=top_k)

    return JsonResponse(
        [
            {
                "title": c.title,
                "provider": c.provider,
                "url": c.url,
                "skills_taught": c.skills_taught,
                "level": c.level,
                "rating": c.rating,
            }
            for c in courses
        ],
        safe=False,
    )


@require_GET
def public_profiles(request):
    """
    GET /api/public_profiles/?q=python&availability=Weekends
    """
    q      = request.GET.get("q", "").lower()
    avail  = request.GET.get("availability")
    qs = StudentProfile.objects.filter(profile_public=True)

    if q:
        qs = qs.filter(skills_offered__icontains=q)
    if avail:
        qs = qs.filter(availability_days__iexact=avail)

    data = [{
        "id": p.id,
        "name": p.user.get_full_name() or p.user.username,
        "location": p.place,
        "skills_offered": p.skills_offered,     # list[str]
        "skills_wanted": p.skills_wanted,
        "rating": p.average_rating,
        "photo_url": p.photo.url if p.photo else "/static/img/default.jpg",
    } for p in qs]

    return JsonResponse(data, safe=False)


# -----------------  CREATE SWAP REQUEST  -----------------
@csrf_exempt
@require_POST
def create_swap(request):
    """
    POST /api/create_swap/
    {
        "requester_id": 1,
        "requestee_id": 7,
        "offered_skill": "Python",
        "wanted_skill": "React"
    }
    """
    import json
    payload = json.loads(request.body)
    swap = SwapRequest.objects.create(
        requester_id   = payload["requester_id"],
        requestee_id   = payload["requestee_id"],
        offered_skill  = payload["offered_skill"],
        wanted_skill   = payload["wanted_skill"],
    )
    return JsonResponse({"ok": True, "swap_id": swap.id})
