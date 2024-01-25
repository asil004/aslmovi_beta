from django.contrib import admin
from django.urls import path, include

from aslmovi.settings.base import BASE_DIR
from aslmovi.settings.local import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

