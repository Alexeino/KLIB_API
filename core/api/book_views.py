from core.api.permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Book
from rest_framework.permissions import IsAdminUser
from .serializers import BookSerializer

# Book Views
class BookListView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    # Get all the Books
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BookSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class BookDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request,pk):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response(
                {"Error 404": "Requested Book Does not Exist."}
            )
        serializer = BookSerializer(book,context={'request':request})
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book,data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Book.DoesNotExist:
            return Response({"Error 404": "Requested Book Does not Exist."})
    
    def delete(self,request,pk):
        permission_classes = [IsAdminUser]
        
        Book.objects.get(id = pk).delete()
        return Response(
            {"Deleted":"Requested Book has been removed."}
        )