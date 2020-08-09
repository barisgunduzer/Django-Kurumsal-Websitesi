from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.models import Post, Category
from home.models import Setting, ContactForm, ContactFormMessage

# Create your views here.


def index(request):
    blogdata = Post.objects.all()[:4]
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'home', 'blogdata': blogdata}
    return render(request, 'index.html', context)


def hakkimizda(request):
    blogdata = Post.objects.all()[:4]
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda', 'blogdata': blogdata}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    blogdata = Post.objects.all()[:4]
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referanslarimiz', 'blogdata': blogdata}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):

    blogdata = Post.objects.all()[:4]
    if request.method == 'POST': #form post edildiyse
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kur
            data.name = form.cleaned_data['name']  # formdan bilgiyi al
            data.name = form.cleaned_data['email']
            data.name = form.cleaned_data['subject']
            data.name = form.cleaned_data['message']
            data.save() # veritabanına kaydet
            messages.success(request, "Mesajınız başarı ile gönderilmiştir.")
            return HttpResponseRedirect('/iletisim')
    setting = Setting.objects.get(pk=1)
    form = ContactForm(request.POST)
    context = {'setting': setting, 'form': form, 'blogdata': blogdata}
    return render(request, 'iletisim.html', context)


def blog(request):
    blogdata = Post.objects.all()[:4]
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'blog','blogdata': blogdata,'category': category}
    return render(request, 'blog.html', context)


def posts(request, slug):
    postdata = Post.objects.get(slug=slug)
    blogdata = Post.objects.all()[:4]
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'blogdata': blogdata,'category': category,'postdata':postdata}
    return render(request, 'blog-detail.html', context)
