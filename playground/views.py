from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from .tasks import notify_customers
# Create your views here.
def say_hello(request):
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Ayodeji'})
