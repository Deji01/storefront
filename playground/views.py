from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)
class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def say_hello(self, request):
        try:
            key = 'httpbin-result'
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data =response.json()
            cache.set(key, data)
            return render(request, 'hello.html', {'name': cache.get(key)})      
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': data})