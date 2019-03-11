from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import authenticate, login, logout


from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .config import USERNAME, API_KEY



from django.contrib.auth.models import User
from .models import Artifact, Comment, Bid, UserProfile
from .forms import ArtifactPostForm, UserForm
from  . import config

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import africastalking, os

# Create your views here.
# @login_required(login_url='/login')
def index(request):
    
    posts = Artifact.objects.all()

    return render(request, 'index.html', {"posts":posts, "current_user":request.user})


def view_artifact(request, artifact_id):
	'''
		view the details of a single artifact
	'''
	# artifact = Artifact.single_artifact(artifact_id)
	artifact = Artifact.objects.get(id = artifact_id)

	return render(request, 'view-artifact.html', {"artifact":artifact})



@login_required
def special(request):
    return HttpResponse("You are logged in !")



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_ = request.POST['emailaddress']
        password_ = request.POST['password']
        user =User.objects.create_user(username, email_, password_)
        user.first_name = username.upper()
        user.last_name = username
        user.save()
        authenticated_user = authenticate(username=username, password=password_)
        login(request, authenticated_user)
        if authenticated_user is not None:
            print("We are in buddy!")
        return redirect(index)

    return render(request, 'registration/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username, password=password_)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})

# @login_required(login_url='/accounts/login')
def post_artifact(request):
    '''
    View function to display a form for creating a post to a authenticated user
    '''
    # current_user = request.user
    posts = Artifact.objects.all()

    if request.method == 'POST':

        name = request.POST['imageName']
        description = request.POST['description']
        file_to_upload = request.POST['imageFile']
        price = request.POST['price']



        form, created = Artifact.objects.get_or_create(name=name, description=description, image=file_to_upload, price=price)
        form.save()
        send_message()
        return redirect(index)
    return render(request, 'post-artifact.html', {"posts":posts})


def place_bid(request, artifact_id):
# def place_bid(request):
    '''
    View function to display a form for placing a bid by an authenticated buyer
    '''
    if request.method == 'POST':
        
        price = request.POST['bid_price']

        image = Artifact.objects.get(id = artifact_id)

        form, created = Bid.objects.get_or_create(bid_price = price, artifact = image, bidder = request.user)
        
        form.save()
       
        return redirect(index)
    return render(request, 'post-artifact.html')


def send_message(request, **args):
    username = config.USERNAME
    
    api_key = config.API_KEY
    
    message = "You posted"
   
    africastalking.initialize(username, api_key)
    
    sms = africastalking.sms
   
    response = sms.send(message, '0707630747')


# def send_message_v1(request, format=None):
#         # send confirmation message to the user
#     username = USERNAME

#     apikey = API_KEY

#     to = '+254707630747'
#     message = ' Hello Bidder'

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

#     return redirect('index')
