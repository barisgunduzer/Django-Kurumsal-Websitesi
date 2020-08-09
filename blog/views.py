from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Post, Category
from home.models import Setting


def show_genres(request):
    return render(request, "blog.html", {'blogdata': Post.objects.all()})
