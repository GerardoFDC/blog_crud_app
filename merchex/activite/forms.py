# listings/forms.py

from django import forms
from activite.models import Blog

class BlogForm(forms.ModelForm):
   class Meta:
     model = Blog
     fields = '__all__'
   