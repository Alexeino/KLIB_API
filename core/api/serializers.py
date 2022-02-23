from rest_framework import serializers
from core.models import Book,Author,Genre,Review

class BookSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name="book-detail")
    class Meta:
        model = Book
        fields = "__all__" 
        
    def save(self,*args,**kwargs):
        genre = self.validated_data.get('genre')
        genre_obj = Genre.objects.get(title = genre)
        genre_obj.books_count += 1
        genre_obj.save()
        return super().save(*args,**kwargs)
        


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exlude = ('books_count',)
        fields = "__all__"
                
class AuthorSerializer(serializers.ModelSerializer):
    # link = serializers.HyperlinkedIdentityField(view_name="author-detail")
    class Meta:
        model = Author
        # exclude = ('slug',)
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name="review-details")
    review_user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = "__all__"
        
