from rest_framework.test import APITestCase
from foodData.models import Product
from django.urls import reverse
from rest_framework import status


class ProductsTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('products')
        self.product_test = Product.objects.create(
            code='te5st4nd0',
            status='DR',
            url='tst.teste.tes.te',
            creator='tester',
            created_t=123456789,
            last_modified_t=234567891,
            product_name='teste',
            generic_name='test',
            quantity='single test'
        )

    def test_list_products(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_not_create_product(self):
        data = {
            'code': 'post',
            'creator': 'should',
            'product_name': 'not',
            'generic_name': 'be',
            'quantity': 'allowed'
        }
        response = self.client.post(self.url, data=data)
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED)
