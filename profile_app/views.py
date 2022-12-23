from django.shortcuts import render
from .forms import UserLoginRegistrationForm
from .utils import send_registration_email
from .models import ConfirmLink
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
import uuid
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
    
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def api_registration(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    form = UserLoginRegistrationForm(data={'email': username,
                                      'password': password})
    profile = form.save(commit=False)
    password = make_password(profile.password)
    profile.password = password
    profile.is_active = False   
    uid =  uuid.uuid4().hex
    url = f'{settings.SITE_LINK}profile/confirm/{uid}'
    profile.save() 
    ConfirmLink.objects.create(uid=uid, user=profile)
    send_registration_email(profile.email, url)
    message = 'check your mail'
    return Response({'message': message},
                    status=HTTP_200_OK)


def registration(request):
    form = UserLoginRegistrationForm(request.POST or None)
    message = 'enter form'
    if request.method == 'POST':
        profile = form.save(commit=False)
        password = make_password(profile.password)
        profile.password = password
        profile.is_active = False   
        uid =  uuid.uuid4().hex
        url = f'{settings.SITE_LINK}profile/confirm/{uid}'
        profile.save()
        login(request, profile)
        ConfirmLink.objects.create(uid=uid, user=profile)
        send_registration_email(profile.email,url)
        message = 'check your mail'
        
    return render(request, 'register.html', {'form': form, 'message': message})


def confirmation(request, uid):
    confirm_link = ConfirmLink.objects.get(uid=uid)
    message = "Your account confirmed"
    if confirm_link.confirmed:
        message = "Your link expired"
        return render(request, 'confirm.html', {'message': message})
    user = confirm_link.user
    user.is_active = True
    user.save()
    confirm_link.confirmed = True
    confirm_link.save()
    return render(request, 'confirm.html', {'message': message})


def private_office(request):
    message = 'Welcome your private office'
    if request.user.is_authenticated:
        return render(request, 'office.html', {'message': message})
    message = 'Please login'
    return render(request, 'office.html', {'message': message})
 
def main(request):
    return render(request, 'main.html')   
    

