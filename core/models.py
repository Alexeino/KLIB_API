from statistics import mode
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
    books_count = models.PositiveIntegerField(null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Genre,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE,null=True,related_name="genres")
    author = models.ForeignKey('Author',on_delete=models.CASCADE,null=True,related_name="authors")
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