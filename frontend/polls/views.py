from django.shortcuts import render
from django.http import HttpResponse
import requests
import logging
from opentelemetry import trace

tracer = trace.get_tracer(__name__)
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    #with tracer.start_as_current_span("index"):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_user_info(request, user_id):
    headers = {k: v for k, v in request.headers.items()}
    logger.error(f"Request headers: {headers}")
    
    #with tracer.start_as_current_span("get_user_info"):
    backend_url = f'http://backend:8080/api/users/{user_id}/'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        user_info = response.json()
        return render(request, 'user_info.html', {'user_info': user_info})
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error fetching user info: {str(e)}", status=500)
