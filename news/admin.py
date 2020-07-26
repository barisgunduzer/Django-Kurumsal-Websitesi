# Register your models here.

from django.contrib import admin
from news.models import Post, Category, Picture

class PostImageInline(admin.TabularInline):
    model = Picture
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['status', 'category']
    inlines = [PostImageInline]

class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Picture,PictureAdmin)


