from django.http import JsonResponse
from opentelemetry import trace

from .models import User

tracer = trace.get_tracer(__name__)

def get_user_info(request, user_id):
    with tracer.start_as_current_span("get_user_info"):
        try:
            user = User.objects.get(id=user_id)  
            data = {
                'username': user.username,
                'email': user.email
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
