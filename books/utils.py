from django.contrib.auth.mixins import UserPassesTestMixin
class UpperCaseTitleMixin:
    """
    Міксін, який перетворює назву книги в контексті на великі літери.
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for book in context['books']:
            book.title = book.title.upper()
        return context


class IsAdminUserMixin(UserPassesTestMixin):
    """
    Міксін, який перевіряє, чи є користувач адміністратором.
    """

    def test_func(self):
        return self.request.user.is_staff



