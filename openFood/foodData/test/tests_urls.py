from rest_framework.test import APITestCase
from foodData.models import Product
from django.urls import reverse
from rest_framework import status


class ProductTestCase(APITestCase):

    def setUp(self):
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

    def test_get_product(self):
        response = self.client.get('/products/4')
        self.assertEquals(response.status_code,
                          status.HTTP_301_MOVED_PERMANENTLY)

    def test_put_product(self):
        data = {
            'code': 'put',
            'creator': 'method',
            'product_name': 'should',
            'generic_name': 'be',
            'quantity': 'allowed'
        }
        response = self.client.put('/products/4', data=data)
        self.assertEquals(response.status_code,
                          status.HTTP_301_MOVED_PERMANENTLY)

    def test_delete_product(self):
        response = self.client.delete('/products/5')
        self.assertEquals(response.status_code,
                          status.HTTP_301_MOVED_PERMANENTLY)
