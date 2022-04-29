from django.test import TestCase
from clothingStore.models import *

class TestModels(TestCase):

    def test_customer_str(self):
        name = Customer.objects.create(name = 'Test Customer')
        self.assertEqual(str(name), 'Test Customer')

    # def test_product_str(self):
    #     name = Product.objects.create(name = 'Test Product')
    #     self.assertEqual(str(name), 'Test Product')