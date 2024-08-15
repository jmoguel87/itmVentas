from django.urls import path
from .views import viewCreateClient,ListClientView,ListClientViewAWS

urlpatterns = [
    path('createNewClient/',viewCreateClient.as_view(),name="createNewClient"),
    path('listClients/',ListClientView.as_view(),name="listClients"),
    path('awslistClients/',ListClientViewAWS.as_view(),name="awslistClients"),

]
