from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Category, Note
from .serializers import NoteSerializer, CategorySerializer


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