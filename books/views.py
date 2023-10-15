# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render

from books.forms import BookForm
from books.models import Book, Genre
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from books.utils import UpperCaseTitleMixin, IsAdminUserMixin
from django.core.paginator import Paginator

def test(request):
    objects = ["john", "paul", "george", "ringo", "john1", "paul2", "george2"]
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'books/books_test.html', {'page_obj': page_objects})

class BookListView(UpperCaseTitleMixin, ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self):
        # Попередній вибір автора і жанру для кожної книги
        return Book.objects.select_related('author', 'genre').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context

class GenreBookListView(ListView):
    model = Book
    template_name = 'books/genre.html'
    context_object_name = 'books'

    def get_queryset(self):
        genre_id = self.kwargs['genre_id']
        # Попередній вибір автора і жанру для кожної книги
        return Book.objects.filter(genre_id=genre_id).select_related('author', 'genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['genre'] = Genre.objects.get(pk=self.kwargs['genre_id'])
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(IsAdminUserMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create_book.html'

    def get_success_url(self):
        return reverse_lazy('books_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Додаємо поточного користувача до контексту
        return context
