from django.shortcuts import render
from .serializers import NoteSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category, Note


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    
class CategoryNotesListView(ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Note.objects.filter(user=self.request.username , category_id=category_id)
    

class NoteListView(ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NoteCreateView(CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)