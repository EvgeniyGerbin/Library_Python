from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')  # URL, на який перенаправляє користувача після успішної реєстрації
    template_name = 'registration/register.html'  # Шаблон, який ви використовуєте для своєї сторінки реєстрації

    def form_valid(self, form):
        print(form.cleaned_data)  # Друкуються дані, які вдало прошли валідацію
        response = super().form_valid(form)
        print(response.status_code)  # Друкує статус коду відповіді
        return response


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')