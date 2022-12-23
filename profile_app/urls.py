from django.urls import path
from .views import registration, confirmation, private_office, login, api_registration

app_name = 'profile_app'

urlpatterns = [ 
    path('register/',registration, name='register'),
    path('confirm/<str:uid>',confirmation),
    path('office/',private_office),
    path('login/', login),
    path('api/register', api_registration)
]