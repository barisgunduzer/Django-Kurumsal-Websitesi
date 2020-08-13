from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, FileInput, TextInput, Select
from blog.models import Post


class ContentForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'keywords', 'description', 'image', 'content', 'slug']
        widgets = {
            'category': Select(attrs={'class': 'input', 'placeholder': 'category'}),
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
            'content': CKEditorWidget(),
            'slug': TextInput(attrs={'class': 'input', 'placeholder': 'slug'}),
        }