from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
   path('', views.index, name='home'),
   path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
   path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item'),
   path('booking/', include(router.urls)),
   path('api-token-auth/', obtain_auth_token),  # Эндпоинт для получения токена
]


