from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.menu1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = MenuItem.objects.create(title="Pizza", price=120, inventory=50)
        
    def test_getall(self):
        response = self.client.get('/api/menu-items/')
        menu_items = MenuItem.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
