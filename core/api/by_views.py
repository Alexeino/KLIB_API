from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Author
from .serializers import AuthorSerializer, BookSerializer
from core.models import Book,Author,Genre

class BooksByAuthor(APIView):
    def get(self,request,slug):
        
        if Author.objects.filter(slug = slug).exists():
            print("Author Exists")
            books = Book.objects.filter(author__slug = slug)
            if books:
                serializer = BookSerializer(books,many=True,context={'request':request})
                return Response(serializer.data)
            else:
                return Response({"Error 404":"No books from this Author"})

        else:
            return Response({
                    "Error 404": "Author does not Exist."
            })
            
    def post(self,request,slug):
        
        if Author.objects.filter(slug = slug).exists():
            author = Author.objects.get(slug = slug)
            serializer = BookSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(author = author)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({
                    "Error 404": "Author does not Exist."
            })

class BooksByGenre(APIView):
    
    def get(self,request,slug):
        if Genre.objects.filter(slug=slug).exists():
            
            books = Book.objects.filter(genre__slug = slug)
            if books:
                serializer = BookSerializer(books,many=True,context={'request':request})
                return Response(serializer.data)
            else:
                return Response({"Error 404":"Books by Requested Genre does not exist."})
        
        else:
            return Response({"Error 404":"Requested Genre does not exist."})
        
    def post(self,request,slug):
        
        if Genre.objects.filter(slug = slug).exists():
            genre = Genre.objects.get(slug = slug)
            print(genre)
            serializer = BookSerializer(data = request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save(genre = genre)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({
                    "Error 404": "Genre does not Exist."
            })
