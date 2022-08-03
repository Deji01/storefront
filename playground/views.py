from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)
class HelloView(APIView):
    def say_hello(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data =response.json()
            return render(request, 'hello.html', {'name': data})
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        
