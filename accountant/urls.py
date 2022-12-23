from django.urls import path
from .views import CategoryListView, NoteListView, NoteCreateView , CategoryNotesListView



app_name = 'accountant'

urlpatterns = [ 
    path('category/', CategoryListView.as_view()),
    path('category/<int:category_id>', NoteListView.as_view()),
    path('note/', NoteListView.as_view()),
    path('note/create', NoteCreateView.as_view()),
]