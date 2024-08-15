from django.contrib import admin
from django.urls import path, include
from apps.clients.views import viewIndex

urlpatterns = [
    path('',viewIndex.as_view(),name="index"),
    path('',include('apps.clients.urls')),
    path('',include('apps.articles.urls')),
    path('admin/', admin.site.urls),
]
