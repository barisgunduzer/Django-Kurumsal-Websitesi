from ckeditor_uploader.forms import SearchForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Category, Comment, Post
from home.forms import SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage

# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.all().order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'home',
               'last_posts': last_posts}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.all().order_by('-id')[:4]
    context = {'setting': setting,
               'page': 'hakkimizda',
               'last_posts': last_posts}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    last_posts = Post.objects.all().order_by('-id')[:4]
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
    last_posts = Post.objects.all().order_by('-id')[:4]
    context = {'setting': setting,
               'form': form,
               'page': 'iletisim',
               'last_posts': last_posts}
    return render(request, 'iletisim.html', context)

def blog(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    post = Post.objects.filter(status=True)
    last_posts = Post.objects.all().order_by('-id')[:4]
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
    comments = Comment.objects.filter(post_id=id, status=True)
    last_posts = Post.objects.all().order_by('-id')[:4]
    context = {'setting': setting,
               'last_posts': last_posts,
               'category': category,
               'post': post,
               'comments': comments,}
    return render(request, 'blog-detail.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/blog')
        else:
            messages.warning(request, "Kullanıcı Adı veya Şifre Yanlış")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    last_posts = Post.objects.all().order_by('-id')[:4]
    context = {'category': category,
               'last_posts': last_posts,
               }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)   #formumuzu signup ile ilişkilendirdik.
        if form.is_valid():               #valid kontrolü yaptık. şifre vs. uymuyorsa kurallara buna takılıyor.
            form.save()                   #kurallar dolu mu boş mu şifreler aynı mı uyuyor mu vs. dorm.save ile tüm elemanları alıp eşleştirdik.
            #return HttpResponse("Üye kaydedildi.") #kontrol ettim.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            #Create data in profile table for user
            current_user = request.user
            data = User()
            data.user_id = current_user.id
            data.image = "images/user/user.png"
            data.save()
            messages.success(request, "Hoş Geldiniz.. Sitemize başarılı bir şekilde üye oldunuz. İyi yolculuklar dileriz.")
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'signup.html', context)