from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_list, name='authors_list'),
]
