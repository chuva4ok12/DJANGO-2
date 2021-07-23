from django.test import TestCase
from mainapp.models import Product, ProductCategory

class ProductsTestCase(TestCase):
   def setUp(self):
       category = ProductCategory.objects.create(name="кухня")
       self.product_1 = Product.objects.create(name="столешница",
                                          category=category,
                                          price = 3455.3,
                                          quantity=103)

       self.product_2 = Product.objects.create(name="кухонный стол",
                                          category=category,
                                          price=2998.1,
                                          quantity=113,
                                          is_active=False)

       self.product_3 = Product.objects.create(name="холодильник",
                                          category=category,
                                          price=21999.9,
                                          quantity=142)

   def test_product_get(self):
       product_1 = Product.objects.get(name="столешница")
       product_2 = Product.objects.get(name="кухонный стол")
       self.assertEqual(product_1, self.product_1)
       self.assertEqual(product_2, self.product_2)

   def test_product_print(self):
       product_1 = Product.objects.get(name="столешница")
       product_2 = Product.objects.get(name="кухонный стол")
       self.assertEqual(str(product_1), 'столешница (кухня)')
       self.assertEqual(str(product_2), 'кухонный стол (кухня)')


   def test_product_get_items(self):
       product_1 = Product.objects.get(name="столешница")
       product_3 = Product.objects.get(name="холодильник")
       products = product_1.get_items()

       self.assertEqual(list(products), [product_1, product_3])

