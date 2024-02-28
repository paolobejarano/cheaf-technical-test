import datetime

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.models import Product, Alert


class ProductTests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Log in the user
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

        self.product = Product.objects.create(
            name="Test Product for Views",
            description="Test Description for Views",
            stock=17,
            expires_at=datetime.date.today() + datetime.timedelta(days=10)
        )

    def test_product_list(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
