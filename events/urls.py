from django.urls import path
from . import views


urlpatterns = [
    # Event URLs
    path('', views.EventList.as_view()),
    path('<int:pk>/', views.EventSingle.as_view()),
    path('admin/', views.AdminEventList.as_view()),
    path('admin/past/', views.AdminEventListPast.as_view()),
    path('admin/<int:pk>/', views.AdminEventSingle.as_view()),
    # Registration URLs
    path('registrations/<int:pk>/', views.RegistrationSingle.as_view())
]
