from django import forms

from authors.models import Author
from books.models import Book, Genre
from django.forms import ModelForm

def validate_title(value):
    if value[0].isdigit():
        raise forms.ValidationError("Назва книги не повинна починатися з цифри.")
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'poster', 'description', 'publication_date', 'author', 'genre']

    title = forms.CharField(
        label="Назва книги",
        validators=[validate_title],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву книги',
        })
    )
    poster = forms.ImageField(label="Зображення обкладинки", required=False, widget=forms.FileInput(attrs={
        'class': 'form-control',
    }))
    description = forms.CharField(label="Опис книги", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введіть опис книги',
    }))
    publication_date = forms.DateField(label="Дата публікації", widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'yyyy-mm-dd',
    }))
    author = forms.ModelChoiceField(label="Автор книги", queryset=Author.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': "Введіть ім'я автора",
    }))
    genre = forms.ModelChoiceField(label="Жанр", queryset=Genre.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
