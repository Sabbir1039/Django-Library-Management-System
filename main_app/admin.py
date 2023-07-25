from django.contrib import admin
from .models import Author, Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country',
                    'date_of_birth', 'date_of_death', 'email', 'website',)
    list_filter = ('country',)
    search_fields = ('name', 'country',)


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'author',
                    'publication_year', 'isbn', 'category', 'description', 'total_copies', 'available_copies',)
    list_filter = ('language', 'category',)
    search_fields = ('title', 'author',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BooksAdmin)
