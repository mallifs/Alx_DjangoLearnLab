# blog/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        # blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Only include title and content in the form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        comment = super().save(commit=False)
        comment.post = self.post
        comment.save()
        return comment
    
    from django import forms
from .models import Post
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    tags = TagField(required=False) 

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


from django import forms
from .models import Post
from taggit.forms import TagField  

class PostForm(forms.ModelForm):
    tags ="TagWidget()" # Use TagField for handling tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include the 'tags' field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),  # Simple text input for tags
        }