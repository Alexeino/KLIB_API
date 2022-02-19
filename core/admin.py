from django.template.defaultfilters import truncatechars
from django.contrib import admin
from .models import Book, Author, Genre
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','genre','author',)
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','slug','title','books_count',)
    
class AuthorAdmin(admin.ModelAdmin):
    
    def about_author(self,obj):
        return f'{obj.about[:100]}...'
    
    list_display = ('id','slug','name','about_author')
    

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre,GenreAdmin)