from django.shortcuts import render
from .serializers import NoteSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category

# Create your views here.

class CategoryListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serialazer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, format=None):
        queryset = Category.objects.all()
        data = CategorySerializer(data=queryset, many=True)        
        return Response(data=data)