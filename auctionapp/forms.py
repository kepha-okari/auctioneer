from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Artifact


class ArtifactPostForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create Post

    '''
    name = forms.CharField(max_length = 10)
    description = forms.CharField(max_length = 10)
    image = forms.ImageField(label='Select a file', help_text='max. 20 megabytes')

    # class Meta:
    #     model = Artifact
    #     fields = ['name','description', 'image']
