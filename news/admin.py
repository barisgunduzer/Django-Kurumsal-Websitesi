# Register your models here.

from django.contrib import admin
from news.models import Post, Category, Picture


class PostImageInline(admin.TabularInline):
    model = Picture
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    readonly_fields = ['image_tag']
    list_filter = ['status']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['status', 'category']


class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Picture, PictureAdmin)


