from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventList.as_view()),
    path('<int:pk>/', views.EventSingle.as_view()),
    path('admin/', views.AdminEventList.as_view()),
    path('admin/<int:pk>/', views.AdminEventSingle.as_view())
]
