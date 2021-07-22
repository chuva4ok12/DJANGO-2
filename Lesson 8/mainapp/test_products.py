from django.test import TestCase
from mainapp.models import Product, ProductCategory


class ProductsTestCase(TestCase):
   def setUp(self):
       category = ProductCategory.objects.create(name="кухня")
       self.product_1 = Product.objects.create(name="столешница",
                                          category=category,
                                          price = 1236.4,
                                          quantity=118)

       self.product_2 = Product.objects.create(name="кухонный шкаф",
                                          category=category,
                                          price=7651.42,
                                          quantity=1215)

       self.product_3 = Product.objects.create(name="вытяжка",
                                          category=category,
                                          price=6542.1,
                                          quantity=125,
                                          is_active=False)


   def test_product_get(self):
       product_1 = Product.objects.get(name="столешница")
       product_2 = Product.objects.get(name="кухонный шкаф")
       self.assertEqual(product_1, self.product_1)
       self.assertEqual(product_2, self.product_2)

   def test_product_print(self):
       product_1 = Product.objects.get(name="столешница")
       product_2 = Product.objects.get(name="кухонный шкаф")
       self.assertEqual(str(product_1), 'столешница (кухня)')
       self.assertEqual(str(product_2), 'кухонный шкаф (кухня)')


   def test_product_get_items(self):
       product_1 = Product.objects.get(name="с")
       product_3 = Product.objects.get(name="вытяжка")
       products = product_1.get_items()

       self.assertEqual(list(products), [product_1, product_3])
