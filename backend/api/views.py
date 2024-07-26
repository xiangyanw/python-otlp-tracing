from django.http import JsonResponse
from opentelemetry import trace
import logging
import os

from .models import User

tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)

def get_user_info(request, user_id):
    headers = {k: v for k, v in request.headers.items()}
    logger.error(f"Request headers: {headers}")

    #with tracer.start_as_current_span("get_user_info"):
    try:
        user = User.objects.get(id=user_id)  
        data = {
            'username': user.username,
            'email': user.email
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
