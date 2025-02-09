from django.contrib.auth.models import User
from rest_framework.test import APIClient
from restaurant.models import Menu
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username='testuser', password='password')
        # Создаем токен для этого пользователя
        self.token = Token.objects.create(user=self.user)
        
        # Создаем элементы меню
        Menu.objects.create(title="Pizza", price=150, inventory=50)
        Menu.objects.create(title="Burger", price=100, inventory=75)

    def test_getall(self):
        client = APIClient()
        
        # Добавляем токен в заголовки запроса
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Запрашиваем данные
        url = reverse('menu-items')
        response = client.get(url)
        
        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ожидаемые данные без поля 'id'
        expected_data = [
            {'title': 'Pizza', 'price': '150.00', 'inventory': 50},
            {'title': 'Burger', 'price': '100.00', 'inventory': 75}
        ]
        
        # Получаем список из ответа без поля 'id'
        response_data = response.json()
        response_data = [{key: value for key, value in item.items() if key != 'id'} for item in response_data]
        
        # Проверяем, что данные в ответе совпадают с ожидаемыми
        self.assertEqual(response_data, expected_data)