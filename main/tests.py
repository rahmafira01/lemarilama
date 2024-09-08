from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_pricey_price_user(self):
        a = Product.objects.create(
          name= "Baggy Jeans",
          price = 150000,
          description = "good quality dan baru satu kali dipakai dan merk zara",
        )
        self.assertTrue(a.is_price_pricey)