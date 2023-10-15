from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import consult_gpt.consult
from authors.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('authors/', include('authors.urls')),
    path('reviews/', include('reviews.urls')),
    path('register/', include('custom_user.urls')),
    path('consult/',consult_gpt.consult.consult, name='consult'),
    path('chat_with_gpt/', consult_gpt.consult.chat_with_gpt, name='chat_with_gpt'),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
