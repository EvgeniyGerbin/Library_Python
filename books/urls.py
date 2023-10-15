from django.urls import path
from books import views
from books.views import BookListView, GenreBookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', BookListView.as_view(), name='books_list'),
    path('genre/<int:genre_id>/', GenreBookListView.as_view(), name='genre_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('add_new_book/', BookCreateView.as_view(), name='add_book')
]
