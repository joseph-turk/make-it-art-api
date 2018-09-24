from django.urls import path
from . import views


urlpatterns = [
    path('', views.ContentList.as_view()),
    path('admin/', views.AdminContentList.as_view()),
    path('admin/<int:pk>/', views.AdminContentSingle.as_view())
]
