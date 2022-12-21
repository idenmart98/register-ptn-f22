from django.urls import path
from .views import CategoryListView


app_name = 'accountant'

urlpatterns = [ 
    path('category/', CategoryListView.as_view()),
]