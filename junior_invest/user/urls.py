from django.urls import path

from . import views


urlpatterns = [
    path('users/me/', views.GetMeView.as_view())
]