from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import Artifact, Comment
from .forms import ArtifactPostForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.

def index(request):
	'''
    View function to display a form for creating a post to a authenticated user
    '''
	posts = Artifact.objects.all()

	return render(request, 'index.html', {"posts":posts})




# @login_required(login_url='/accounts/login')
def post_artifact(request):
    '''
    View function to display a form for creating a post to a authenticated user
    '''
    # current_user = request.user

    if request.method == 'POST':

        name = request.POST['imageName']
        description = request.POST['description']
        file_to_upload = request.POST['imageFile']
        price = request.POST['price']

   

        form, created = Artifact.objects.get_or_create(name=name, description=description, image=file_to_upload, price=price)
        form.save()
        return redirect(index)
    return render(request, 'post-artifact.html')
