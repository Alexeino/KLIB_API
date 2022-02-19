from django.db import models
from django.utils.text import slugify 

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
    
    def __str__(self):
        return self.title