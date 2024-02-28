import datetime

from django.test import TestCase
from freezegun import freeze_time

from main.models import Product, Alert


class ProductTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            stock=10,
            expires_at=datetime.date.today() + datetime.timedelta(days=10)
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.expires_at, datetime.date.today() + datetime.timedelta(days=10))

    def test_alert_creation(self):
        # Test first alert 10 day before expiration
        first_alert = Alert.objects.filter(product=self.product, days_before=10)
        self.assertEqual(first_alert.count(), 1)

        # Test second alert 5 day before expiration
        second_alert = Alert.objects.filter(product=self.product, days_before=5)
        self.assertEqual(second_alert.count(), 1)


class AlertTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product for Alerts",
            description="Test Description for Alerts",
            stock=10,
            expires_at=datetime.date(2024, 3, 27)
        )

        self.alert = Alert.objects.create(
            product=self.product,
            days_before=7
        )

    @freeze_time("2024-02-28")
    def test_alert_active(self):
        self.assertTrue(self.alert.active)

    @freeze_time("2024-03-20")
    def test_alert_expired(self):
        self.assertTrue(self.alert.expired)

    @freeze_time("2024-03-10")
    def test_alert_days_until_activation(self):
        self.assertEqual(self.alert.days_until_activation, 10)

    @freeze_time("2024-03-25")
    def test_alert_days_since_activation(self):
        self.assertEqual(self.alert.days_since_activation, 5)

    @freeze_time("2024-03-20")
    def test_alert_alert_at(self):
        self.assertEqual(self.alert.alert_at, datetime.date(2024, 3, 20))
