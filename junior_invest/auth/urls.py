from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views


urlpatterns = [
    path('token/', views.TokenPairObtainView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]