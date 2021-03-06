from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('artwork/', include('artwork.urls')),
    path('events/', include('events.urls')),
    path('content/', include('content.urls')),
    path('lessons/', include('lessons.urls')),
    path('admin/', admin.site.urls),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
