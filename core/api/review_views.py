from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from core.models import Review,Book
from .serializers import ReviewSerializer
from .permissions import ReviewOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookReviews(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,pk):
        book = Book.objects.filter(id=pk).exists()
        if not book:
            return Response(
                {"Error 404":"Book not found..."}
            )
        reviews = Review.objects.filter(book__id=pk)
        if not reviews:
            return Response(
                {"Error 404":"No Reviews Found for this Book..."}
            )
        serializer = ReviewSerializer(reviews,many=True,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request,pk):
        book = Book.objects.get(id = pk)
        review_user = request.user
        review_queryset = Review.objects.filter(book = book, review_user = review_user).exists()
        
        if review_queryset:
            raise ValidationError("You have already reviewed this book.")
        
        if book:
            serializer = ReviewSerializer(data = request.data,context={'request':request})
            if serializer.is_valid():
                if book.rating_count == 0:
                    book.avg_rating = serializer.validated_data['rating']
                else:
                    book.avg_rating = (book.avg_rating + serializer.validated_data['rating'])/2

                book.rating_count += 1
                book.save()

                serializer.save(review_user = request.user,book=book)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
            
class ReviewDetails(APIView):
    permission_classes = [ReviewOwnerOrReadOnly]
    def get(self,request,pk):
        try:
            review = Review.objects.get(id=pk)
            serializer = ReviewSerializer(review,context={'request':request})
            return Response(serializer.data)
        except Review.DoesNotExist:
            return Response(
                {"Error 404":"Review Does Not Exist with this ID..."}
            )
            
    def put(self,request,pk):
        try:
            review = Review.objects.get(id=pk)
            serializer = ReviewSerializer(review,data = request.data)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save(review_user = request.user,book = review.book)
                return Response(serializer.data)
        except Review.DoesNotExist:
            return Response(
                {"Error 404":"Review Does Not Exist with this ID..."}
            )
    
    def delete(self,request,pk):
        Review.objects.get(id=pk).delete()
        return Response(
            {"SUCCESS 204":"Review Deleted Succesfully.."}
        )