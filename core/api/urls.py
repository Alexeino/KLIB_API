from django.urls import path
from .book_views import BookDetailView, BookListView
from .author_views import AuthorListView,AuthorDetailView
from .by_views import *
from .genre_views import *
urlpatterns = [
    # Books
    path('list/books/',BookListView.as_view(),name="book-list"),
    path('book/<int:pk>/',BookDetailView.as_view(),name="book-detail"),
    
    # Authors
    path('list/authors/',AuthorListView.as_view(),name="author-list"),
    path('author/<slug:slug>/',AuthorDetailView.as_view(),name="author-detail"),
    
    # Genres
    path('list/genres/',GenreListView.as_view(),name="genre-list"),
    path('genre/<slug:slug>/',GenreDetailView.as_view(),name="genre-detail"),
    
    # Books By Author
    path('list/books/author/<slug:slug>',BooksByAuthor.as_view(),name="booksby-author"),
    path('list/books/genre/<slug:slug>',BooksByGenre.as_view(),name="booksby-genre")
    
]
