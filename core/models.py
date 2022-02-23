from django.db.models.signals import post_save,post_delete
from django.db import models
from django.utils.text import slugify 
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    slug = models.SlugField(unique=True,blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Author,self).save(*args,**kwargs)
    
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    books_count = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Genre,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE,related_name="genres",blank=True)
    author = models.ForeignKey('Author',on_delete=models.CASCADE,related_name="authors",blank=True)
    avg_rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    review_user = models.ForeignKey(User,on_delete=models.CASCADE,name="review_user")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,name="book")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.book.title}  {self.rating}'
    
    
def genre_book_decrement(sender,instance,*args,**kwargs):
    print(instance.genre)
    genre = Genre.objects.get(title = instance.genre)
    genre.books_count -= 1
    genre.save()
    
    
post_delete.connect(genre_book_decrement,sender=Book)