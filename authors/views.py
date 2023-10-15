

from django.shortcuts import render
from .models import Author

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/authors_list.html', {'authors': authors})

def home_page(request):
    return render(request, 'home.html')