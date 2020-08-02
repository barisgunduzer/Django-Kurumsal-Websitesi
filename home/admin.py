# Register your models here.

from django.contrib import admin
from home.models import Setting


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


admin.site.register(Setting)
