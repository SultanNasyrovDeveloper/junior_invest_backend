from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/project/', include('junior_invest.project.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
