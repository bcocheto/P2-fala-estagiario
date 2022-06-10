from datetime import datetime

from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titlePost', 'bodyPost', 'userName']
        widgets = {
            'userName': forms.TextInput(
                attrs={'id': 'userName', 'required': True, 'placeholder': 'Nome de usuário'}
            ),
            'titlePost': forms.TextInput(
                attrs={'id': 'titlePost', 'required': True, 'placeholder': 'Título'}
            ),
            'bodyPost': forms.TextInput(
                attrs={'id': 'bodyPost', 'required': True, 'placeholder': 'Diga algo...'}
            ),
        }
