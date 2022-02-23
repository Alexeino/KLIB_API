from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.permissions import IsAdminOrReadOnly
from core.models import Author
from rest_framework.permissions import IsAdminUser
from .serializers import AuthorSerializer

class AuthorListView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self,request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
class AuthorDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self,request,slug):
        try:
            author = Author.objects.get(slug=slug)
        except Author.DoesNotExist:
            return Response({"Error 404":"Requested Author does not Exist."})
        
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    def put(self,request,slug):
        author = Author.objects.get(slug=slug)
        serializer = AuthorSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,slug):
        permission_classes = [IsAdminUser]
        
        Author.objects.get(slug = slug).delete()
        return Response(
            {"Deleted":"Requested Author has been removed."}
        )