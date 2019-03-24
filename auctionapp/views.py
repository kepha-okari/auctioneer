from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import authenticate, login, logout
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from django.contrib.auth.models import User
from .models import Artifact, Comment, Bid, UserProfile, Category
from .forms import ArtifactPostForm, UserForm
from  . import config

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import africastalking, os

def index(request):

    profile = UserProfile.objects.get(user=request.user.id)

    print(profile.profile_pic.url)

    categories = Category.get_categories
    
    posts = Artifact.objects.all()

    return render(request, 'index.html', {"profile":profile , "posts":posts, "current_user":request.user, "categories":categories })

def search_results(request):
    categories = Category.get_categories
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        posts = Artifact.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'results.html', {"posts":posts, "current_user":request.user, "categories":categories })

    else:
        message = "You haven't searched for any term"
        return render(request, 'results.html', {"message":message})



def list_by_category(request, category_id):

    posts = Artifact.get_images_by_category(category_id)

    return render(request, 'index.html', {"posts":posts, "current_user":request.user})




def view_artifact(request, artifact_id):
	'''
		view the details of a single artifact
	'''
	artifact = Artifact.single_artifact(artifact_id)

	return render(request, 'view-artifact.html', {"artifact":artifact})


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_ = request.POST['email']
        password_ = request.POST['password']
        user =User.objects.create_user(username, email_, password_)
        user.first_name = username.upper()
        user.last_name = username
        user.save()

        authenticated_user = authenticate(username=username, password=password_)
        login(request, authenticated_user)

        if authenticated_user is not None:
            print("We are in buddy! KARIBU")
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
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})

@login_required(login_url='/login')
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
        # send_message()
        return redirect(single_artifact)
    return render(request, 'post-artifact.html', {"posts":posts})


def place_bid(request, artifact_id):
    '''
    View function to display a form for placing a bid by an authenticated buyer
    '''
    if request.method == 'POST':

        current_user = request.user
        
        price = request.POST['bid_price']

        image = Artifact.objects.get(id = artifact_id)

        # number = UserProfile.objects.get(user = request.user)

        # if number.phone_number is None:
        #     print('Hi {}, Please include your phone contact on your profile'.format(request.user))
        # else:
        #     print('number is: {}'.format(number.phone_number))

        message = 'Hi {0}, you have placed a Kshs {1} bid on {2} at Auctioneer.com'.format(current_user, price, image.name)

        

        form, created = Bid.objects.get_or_create(bid_price = price, artifact = image, bidder = current_user)
        
        form.save()

        send_message(request, message)

        return redirect(index)
    return render(request, 'post-artifact.html')


def comment(request, artifact_id):
    '''
    View function to display a form for placing a bid by an authenticated buyer
    '''
    if request.method == 'POST':

        current_user = request.user
        
        text = request.POST['comment']

        artifact = Artifact.objects.get(id = artifact_id)

        form, created = Comment.objects.get_or_create(posted_by = current_user, artifact = artifact, comment = text)
        
        form.save()

        return redirect(index)
    return render(request, 'post-artifact.html')


def send_message(request, message):

    username = config.USERNAME
    
    api_key = config.API_KEY

    to = UserProfile.objects.get(user = request.user).phone_number
    
    message = message

    gateway = AfricasTalkingGateway(username, api_key)

    try:
        results = gateway.sendMessage(to, message)

        for recipient in results:
            # status is either "Success" or "error message"
            print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost']))

    except AfricasTalkingGatewayException as e:
        print('Encountered an error while sending: %s' % str(e))


