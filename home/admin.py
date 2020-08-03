# Register your models here.

from django.contrib import admin
from home.models import Setting, ContactFormMessage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(Setting)
