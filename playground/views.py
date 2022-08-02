from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
# Create your views here.
def say_hello(request):
    try:
        message = EmailMessage('subject', 'message', 'info@dejibuy.com', ['yo@dejibuy.com'])
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Ayodeji'})
