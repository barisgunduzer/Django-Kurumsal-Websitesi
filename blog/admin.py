# Register your models here.

from django.contrib import admin

from blog.models import BlogPicture, BlogCategory, BlogPost


class PostImageInline(admin.TabularInline):
    model = BlogPicture
    extra = 3


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    readonly_fields = ['image_tag']
    list_filter = ['status']


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['status', 'category']


class BlogPictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPicture, BlogPictureAdmin)
