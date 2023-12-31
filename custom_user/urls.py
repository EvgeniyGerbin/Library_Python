from django.urls import path
from .views import RegisterView, login_view, logout_view

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
