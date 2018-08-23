from django import forms
from .models import Blog

class BlogPostForm(forms.ModelForm):
    
    title = forms.CharField(label='Título')
    content = forms.CharField(label='Texto')
    image = forms.ImageField(label='imagen')
    tag = forms.CharField(label='Etiquetas(#)')
    
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'tag')
        
