from django.urls import path
from .views import ArticleListView,ArticleDetailView,ArticleUpdateView,ArticleDeleteView,ArticleCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
     path("<int:pk>/", ArticleDetailView.as_view(),
        name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(),
        name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(),
        name="article_delete"),
    path("new/", ArticleCreateView.as_view(), name="article_new"), 
    path("", ArticleListView.as_view(), name="article_list"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
