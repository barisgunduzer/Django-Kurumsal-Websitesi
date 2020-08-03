from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactForm, ContactFormMessage


# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referanslarimiz'}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):

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
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)
