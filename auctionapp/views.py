from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import Artifact, Comment, Bid
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


def view_artifact(request, artifact_id):
	'''
		view the details of a single artifact
	'''
	# artifact = Artifact.single_artifact(artifact_id)
	artifact = Artifact.objects.get(id = artifact_id)

	return render(request, 'view-artifact.html', {"artifact":artifact})



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


# def place_bid(request, artifact_id):
def place_bid(request):
    '''
    View function to display a form for placing a bid by an authenticated buyer
    '''
    # current_user = request.user

    if request.method == 'POST':
        price = request.POST['bid_price']
        # form, created = Bid.objects.get_or_create(bid_price=price, artifact=artifact_id)
        form, created = Bid.objects.get_or_create(bid_price=price)
        form.save()
        return redirect(index)
    return render(request, 'post-artifact.html')


# def send_message(request, *args):
#  	"""
# 		Function to haundle messaging
#  	"""
#     username = username1
#     apikey = apikey1
#     to = user_contact
#     message = 'Congratulations '+ request.user.username.upper() +'for showing interest on my art work.\n' 'We will be able to tell the highest bid in the next '+ str(when)[:10] + ' at ' + str(when)[11:16]


#     gateway = AfricasTalkingGateway(username, apikey)

#     try:
#         # Thats it, hit send and we'll take care of the rest.

#         results = gateway.sendMessage(to, message)

#         for recipient in results:
#             # status is either "Success" or "error message"
#             print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
#                                                                 recipient['status'],
#                                                                 recipient['messageId'],
#                                                                 recipient['cost']))

#     except AfricasTalkingGatewayException as e:
#         print('Encountered an error while sending: %s' % str(e))


# def schedule_bid(request, *args):
# 	pass