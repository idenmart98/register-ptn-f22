from django.core.mail import send_mail
from django.conf import settings


def send_registration_email(email,message):
    a = send_mail(
        subject = 'registration email',
        message = message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email,] 
     )
