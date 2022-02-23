from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Genre
from .serializers import GenreSerializer
from core.api.permissions import IsAdminOrReadOnly

class GenreListView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self,request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = GenreSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class GenreDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request,slug):
        try:
            genre = Genre.objects.get(slug=slug)
        except Genre.DoesNotExist:
            return Response(
                {"Error 404":"Requested Genre does not Exist"}
            )
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self,request,slug):
        genre = Genre.objects.get(slug=slug)
        serializer = GenreSerializer(genre,data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
        
    def delete(self,request,slug):
        Genre.objects.get(slug = slug).delete()
        return Response(
            {"Deleted":"Requested Genre has been removed."}
        )      