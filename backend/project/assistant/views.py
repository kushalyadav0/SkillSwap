import json, joblib, os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chat import get_chat_response
from .recsys.rank_profiles import rank_candidates

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
