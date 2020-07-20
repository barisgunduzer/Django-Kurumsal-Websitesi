from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text = "<b>Django Kurulumu : </b>" \
           "python -m pip install -e django <br>" \
           "<b>Proje Oluşturma : </b>" \
           "django-admin startproject mysite <br>" \
           "<b>App Ekleme : </b>" \
           "python manage.py startapp polls"
    context = {'text': text}
    return render(request, 'index.html', context)
