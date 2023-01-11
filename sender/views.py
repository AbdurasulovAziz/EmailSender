from EmailSender.celery import send_email
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from sender.forms import EmailForm
# Create your views here.




class HomePage(APIView):
    def get(self, request):
        return render(request, 'sender/base.html', {'form':EmailForm})

    def post(self, request):
        title = request.data.get('title')
        text = request.data.get('text')
        emails = request.data.get('emails').replace(' ', ',').replace('\r\n', '').split(',')
        for index in range(len(emails)):
            try:
                validate_email(emails[index])
            except ValidationError as e:
                return Response({'error': e})

        send_email.delay(title, text, emails)
        return Response({'data':'success'})