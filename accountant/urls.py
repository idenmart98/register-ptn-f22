from django.urls import path
from .views import CategoryListView, NoteListView



app_name = 'accountant'

urlpatterns = [ 
    path('category/', CategoryListView.as_view()),
    path('note/', NoteListView.as_view()),
]