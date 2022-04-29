
from urllib import request, response
from wsgiref.util import request_uri
from django.test import TestCase, Client
from django.urls import reverse
from clothingStore.views import *
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.dashboard_url = reverse('dashboard')
        self.checkout_url = reverse('checkout')
        self.confirmorder_url = reverse('confirmorder')
        self.updateItem_url = reverse('updateItem')
        self.processOrder_url = reverse('processOrder')


    def test_loginUser_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clothingStore/loginUser.html')

    def test_loginUser_POST(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpass'})

        self.assertEqual(response.status_code, 200)

    

    def test_logoutUser_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEqual(response.status_code, 302)

    def test_dashboard_GET(self):
        response = self.client.get(self.dashboard_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clothingStore/dashboard.html')

    def test_checkout_GET(self):
        response = self.client.get(self.checkout_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clothingStore/checkout.html')

    def test_confirmorder_GET(self):
        response = self.client.get(self.confirmorder_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clothingStore/confirmOrder.html')

    def test_updateItem_GET(self):
        sample_json = {'form': {'name': None, 'email': None, 'total': '1100.00'}, 'shipping': {'address': 'Road no: Dhanmondi 7/A', 'city': 'Dhaka', 'area': 'Dhanmondi', 'zipcode': '1209'}}
        data = (json.loads(request.body))
        print("DATA ",data)
        sample_json = json.dump(sample_json, ensure_ascii=False)
        # path = /path/to/file
        # filename = testcase.json
        self.assertEqual(data, sample_json)

        self.assertEqual(response.status_code, 302)
        

    def test_processOrder_GET(self):
        sample_json = {'productId': '1', 'action': 'remove'}
        data = (json.loads(request.body))
        print("DATA ",data)
        sample_json = json.dump(sample_json, ensure_ascii=False)
        # path = /path/to/file
        # filename = testcase.json
        self.assertEqual(data, sample_json)

        self.assertEqual(response.status_code, 302)




    