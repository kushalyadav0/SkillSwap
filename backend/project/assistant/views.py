from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .chat import get_chat_response

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        if user_message:
            response = get_chat_response(user_message)
            return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)
