from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('auth/', include('djoser.urls')),  # Маршруты Djoser
    path('auth/', include('djoser.urls.authtoken')),  # Маршруты для токенов
]