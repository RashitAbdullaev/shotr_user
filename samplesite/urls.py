from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('test_django_url.urls')),
    path('admin/', admin.site.urls),
]