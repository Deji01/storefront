from django.shortcuts import render
import requests

# Create your views here.
def say_hello(request):
    requests.get('https://httpbin.org/delay/2')
    return render(request, 'hello.html', {'name': 'Ayodeji'})
