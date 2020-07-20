# Register your models here.

from django.contrib import admin
from news.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin)
