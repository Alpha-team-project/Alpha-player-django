from django import forms
from .models import Category, Author, Music

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
        }
        labels = {
            'name': 'Category Name',
        }

# Form for Author model
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'image', 'description']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter author description'
            }),
        }
        labels = {
            'full_name': 'Full Name',
            'image': 'Profile Image',
            'description': 'Description',
        }

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'author', 'description', 'length', 'file', 
                 'lyrics', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter music title'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter description'
            }),
            'length': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Length in seconds'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
            'lyrics': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Enter lyrics'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
        }
        labels = {
            'title': 'Title',
            'author': 'Author',
            'description': 'Description',
            'length': 'Length (seconds)',
            'file': 'Audio File',
            'lyrics': 'Lyrics',
            'category': 'Category',
            'image': 'Cover Image',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MusicForm, self).__init__(*args, **kwargs)
        # limits authors to the current user's author profile
        if user and hasattr(user, 'author_profile'):
            self.fields['author'].queryset = Author.objects.filter(user=user)