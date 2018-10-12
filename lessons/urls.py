from django.urls import path
from . import views


urlpatterns = [
    path('', views.LessonList.as_view()),
    path('<int:pk>/', views.LessonSingle.as_view()),
    path('tags/', views.TagList.as_view()),
    path('admin/', views.AdminLessonList.as_view()),
    path('admin/<int:pk>/', views.AdminLessonSingle.as_view()),
    path('admin/tags/', views.AdminTagList.as_view()),
    path('admin/tags/<int:pk>/', views.AdminTagSingle.as_view())
]
