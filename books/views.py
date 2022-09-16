from django.shortcuts import render
from django.views import generic
from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price']
