from django.shortcuts import render
from .forms import UserLoginRegistrationForm
from .utils import send_registration_email
from .models import ConfirmLink
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
import uuid

def registration(request):
    form = UserLoginRegistrationForm(request.POST or None)
    message = 'enter form'
    if request.method == 'POST':
        profile = form.save(commit=False)
        password = make_password(profile.password)
        profile.password = password
        profile.is_active=False   
        uid =  uuid.uuid4().hex
        url = f'{settings.SITE_LINK}profile/confirm/{uid}'
        profile.save()
        login(request, profile)
        ConfirmLink.objects.create(uid=uid, user=profile)
        send_registration_email(profile.email,url)
        message = 'check your mail'
        
    return render(request,'register.html',{'form': form, 'message': message})


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
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'office.html', {'message': message})
    message = 'Please login'
    return render(request, 'office.html', {'message': message})
 
def main(request):
    return render(request, 'main.html')   
    

