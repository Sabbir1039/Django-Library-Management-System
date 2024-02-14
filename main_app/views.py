from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm
from .models import Author, Book
from .filters import AuthorFilter, BookFilter
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required


# view function for home
def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    total_author = authors.count()
    total_book = books.count()
    context = {
        'total_author': total_author,
        'total_book': total_book,
    }
    return render(request, 'main_app/home.html', context)


# Show all authors data
def authors(request):
    authors = Author.objects.all()
    author_filter = AuthorFilter(request.GET, queryset=authors)
    authors = author_filter.qs
    context = {
        'authors': authors,
        'author_filter': author_filter,
    }
    return render(request, 'main_app/authors.html', context)


# Show all books data
def books(request):
    books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=books)
    books = book_filter.qs
    context = {
        'books': books,
        'book_filter': book_filter,
    }
    return render(request, 'main_app/books.html', context)


# Add authors to database using forms
@login_required(login_url='login')
@permission_required('user_accounts.is_librarian', raise_exception=True)
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Author: {name} successfully added!')
            return redirect('allAuthors')
    else:
        form = AuthorForm()
        context = {
            'form': form,
            'title': 'Add Author',
        }
        return render(request, 'main_app/author_form.html', context)


# Add book to database using forms
@login_required(login_url='login')
@permission_required('user_accounts.is_librarian', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Book: {title} successfully added!')
            return redirect('allBooks')
    else:
        form = BookForm()
        title = 'Add Book'
        context = {
            'form': form,
            'title': title,
        }
        return render(request, 'main_app/book_form.html', context)


# Show details of Author
# @login_required(login_url='login')
def author_details(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {
        'author': author,
    }
    return render(request, 'main_app/author_details.html', context)


# update Author
@login_required(login_url='login')
@permission_required('user_accounts.is_librarian', raise_exception=True)
def update_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f"{name}'s profile successfully updated!")
            return redirect('authorDetails', author_id=author_id)
    else:
        form = AuthorForm(instance=author)
        title = f'Update Author: {author.name}'
        context = {
            'form': form,
            'title': title
        }
        return render(request, 'main_app/author_form.html', context)


# Delete Author
@login_required(login_url='login')
@permission_required('user_accounts.is_librarian', raise_exception=True)
def delete_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    if request.method == "POST":
        author.delete()
        author = author.name
        messages.success(request, f'Book: {author} Successfully Deleted!')
        return redirect('allAuthors')
    else:
        return render(request, 'main_app/delete_author_confirm.html', {'author': author})


# Show book details
# @login_required(login_url='login')
def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book,
    }
    return render(request, 'main_app/book_details.html', context)


# Update book details
@login_required(login_url='login')
@permission_required('user_accounts.is_librarian', raise_exception=True)
def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Book: {title} Successfully Updated!')
            return redirect('bookDetails', book_id=book_id)
    else:
        form = BookForm(instance=book)
        title = f'Update Book, {book.title}'
        context = {
            'form': form,
            'title': title,
        }
        return render(request, 'main_app/book_form.html', context)


# Delete book
@login_required(login_url='login')
@permission_required('user_accounts.is_librarian', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        book.delete()
        book = book.title
        messages.success(request, f'Book: {book} Successfully Deleted!')
        return redirect('allBooks')
    else:
        return render(request, 'main_app/delete_book_confirm.html', {'book': book})


