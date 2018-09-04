from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArtworkList.as_view()),
    path('<int:pk>/', views.ArtworkSingle.as_view()),
    path('admin/', views.AdminArtworkList.as_view()),
    path('admin/<int:pk>/', views.AdminArtworkSingle.as_view())
]
