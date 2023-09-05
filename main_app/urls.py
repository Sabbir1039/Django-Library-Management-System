from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('add_author', views.add_author, name='addAuthor'),
    path('add_book', views.add_book, name='addBook'),

    path('authors', views.authors, name="allAuthors"),
    path('books', views.books, name="allBooks"),

    path('author_details/<int:author_id>',
         views.author_details, name='authorDetails'),
    path('update_author/<int:author_id>',
         views.update_author, name='updateAuthor'),
    path('delete_author/<int:author_id>',
         views.delete_author, name='deleteAuthor'),

    path('book_details/<int:book_id>', views.book_details, name='bookDetails'),
    path('update_book/<int:book_id>', views.update_book, name="updateBook"),
    path('delete_book/<int:book_id>', views.delete_book, name="deleteBook"),
]
