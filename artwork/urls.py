from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ArtworkList.as_view()),
    path('single/<int:pk>/', views.ArtworkSingle.as_view())
]
