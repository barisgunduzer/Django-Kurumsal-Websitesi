from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Category, Comment, Picture
from home.models import Setting, ContactForm, ContactFormMessage

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.all()[:4]
    context = {'setting': setting,
               'page': 'home',
               'last_posts': last_posts}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.all()[:4]
    context = {'setting': setting,
               'page': 'hakkimizda',
               'last_posts': last_posts}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.all()[:4]
    context = {'setting': setting,
               'page': 'referanslarimiz',
               'last_posts': last_posts}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    if request.method == 'POST':  #form post edildiyse
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
    last_posts = Post.objects.all()[:4]
    context = {'setting': setting,
               'form': form,
               'last_posts': last_posts}
    return render(request, 'iletisim.html', context)

def blog(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    post = Post.objects.filter(status=True)
    last_posts = Post.objects.all()[:4]
    context = {'setting': setting,
               'page': 'blog',
               'last_posts': last_posts,
               'category': category,
               'post': post}
    return render(request, 'blog.html', context)

def blog_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post_id=id,status=True)
    last_posts = Post.objects.all()[:4]
    context = {'setting': setting,
               'last_posts': last_posts,
               'category': category,
               'post': post,
               'comments': comments}
    return render(request, 'blog-detail.html', context)
