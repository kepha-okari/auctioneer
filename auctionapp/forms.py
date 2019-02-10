from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Artifact


class ArtifactPostForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create Post
    '''
    class Meta:
        model = Artifact
        fields = ['name','description', 'image']
