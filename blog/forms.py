
from django import forms

from .models import Post, Category

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','link','category','calorie','material','text','time','process','motion','ingredients','carbohydrate','protein','lipid','image1','image2','image3','image4')

