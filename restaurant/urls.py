from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

# Инициализация роутера
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),  # Получение всех меню
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item'),  # Получение одного элемента меню по ID
    path('booking/', include(router.urls)),  # Все URL для Booking, например /tables/ для списка
    path('api-token-auth/', obtain_auth_token),  # Эндпоинт для получения токена
]