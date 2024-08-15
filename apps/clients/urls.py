from django.urls import path
from .views import viewCreateClient,ListClientView

urlpatterns = [
    path('createNewClient/',viewCreateClient.as_view(),name="createNewClient"),
    path('listClients/',ListClientView.as_view(),name="listClients"),
]
