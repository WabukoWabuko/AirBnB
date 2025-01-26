from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
import os

urlpatterns = [
    path('check-static/', lambda request: HttpResponse(
        '\n'.join(os.listdir(settings.STATIC_ROOT)),
        content_type='text/plain'
    )),
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
]
