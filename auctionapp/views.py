from django.shortcuts import render,redirect
# from django.http import Http404, HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from .models import Profile,Image,Comment,Like,Follow
# from .forms import ImagePostForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.

def index():
	return render(reqest, 'index.html')


# @login_required(login_url='/accounts/login')
# def new_post(request):
#     '''
#     View function to display a form for creating a post to a authenticated user
#     '''
#     current_user = request.user

#     if request.method == 'POST':

#         form = ImagePostForm(request.POST, request.FILES)

#         if form.is_valid:
#             post = form.save(commit=False)
#             post.user = current_user
#             post.save()
#             return redirect(profile)
#     else:
#         form = ImagePostForm()
#     return render(request, 'new-post.html', {"form":form})
