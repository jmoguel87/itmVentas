from django.urls import path
from .views import viewCreateArticle,ListArticleView

urlpatterns = [
    path('createNewArticle/',viewCreateArticle.as_view(),name="createNewArticle"),
    path('listArticles/',ListArticleView.as_view(),name="listArticles"),
]
