
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','calorie','material','text','time','process','motion','ingredients')

