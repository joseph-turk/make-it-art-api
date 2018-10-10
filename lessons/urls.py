from django.urls import path
from . import views


urlpatterns = [
    path('', views.LessonList.as_view()),
    path('<int:pk>/', views.LessonSingle.as_view()),
    path('tags/', views.TagList.as_view())
]
