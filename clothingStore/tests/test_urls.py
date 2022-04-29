from django.test import SimpleTestCase
from django.urls import reverse, resolve
from clothingStore.views import *

class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse ('login')
        self.assertEquals(resolve(url).func, loginUser)

    def test_logout_url_is_resolved(self):
        url = reverse ('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_dashboard_url_is_resolved(self):
        url = reverse ('dashboard')
        self.assertEquals(resolve(url).func, dashboard)

    def test_checkout_url_is_resolved(self):
        url = reverse ('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_confirmorder_url_is_resolved(self):
        url = reverse ('confirmorder')
        self.assertEquals(resolve(url).func, confirmorder)

    def test_updateItem_url_is_resolved(self):
        url = reverse ('updateItem')
        self.assertEquals(resolve(url).func, updateItem)

    def test_processOrder_url_is_resolved(self):
        url = reverse ('processOrder')
        self.assertEquals(resolve(url).func, processOrder)