from django.shortcuts import render
from .forms import UserRegistrationForm
from .utils import send_registration_email
from .models import ConfirmLink
from django.conf import settings
import uuid

def registration(request):
    form = UserRegistrationForm(request.POST or None)
    message = 'enter form'
    if request.method == 'POST':
        profile = form.save(commit=False)
        profile.is_active=False    
        url = f'{settings.SITE_LINK}profile/confirm/{uuid.uuid4().hex}'
        profile.save()
        ConfirmLink.objects.create(uid=url, user=profile)
        send_registration_email(profile.email,url)
        message = 'check your mail'
        
    return render(request,'register.html',{'form': form, 'message': message})




