from rest_framework import serializers
from core.models import Book,Author,Genre

class BookSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name="book-detail")
    class Meta:
        model = Book
        fields = "__all__" 

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exlude = ('books_count',)
        fields = "__all__"
                
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # exclude = ('slug',)
        fields = "__all__"
