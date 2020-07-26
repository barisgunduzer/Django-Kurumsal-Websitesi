# Register your models here.

from django.contrib import admin

from news.models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']
    list_filter = ['status','category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

