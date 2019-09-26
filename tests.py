from django.test import TestCase
from leitor_tab.models import Sale
import os

class TestSale(TestCase):

    def test_upload(self):
        upload_file = open(os.getcwd() + '/leitor_tab/static/arquivos/example_input.tab', 'rb')
        response = self.client.post("/importar", data={'file_upload': upload_file})

        self.assertEqual(response.context['status'], 200)


    def test_upload_save_object(self):
        upload_file = open(os.getcwd() + '/leitor_tab/static/arquivos/example_input.tab', 'rb')
        response = self.client.post("/importar", data={'file_upload': upload_file})

        sale = Sale.objects.filter( purchaser_name='Snake Plissken',
                                    item_description='R$20 Sneakers for R$5',
                                    item_price=5.0,
                                    purchase_count=4,
                                    merchant_address='123 Fake St',
                                    merchant_name='Sneaker Store Emporium')

        self.assertEqual(sale.count(), 1)


    def test_upload_without_file(self):
        upload_file = open(os.getcwd() + '/leitor_tab/static/arquivos/example_input.tab', 'rb')
        response = self.client.post("/importar")

        self.assertEqual(response.context['status'], 400)

    
    def test_upload_null(self):
        upload_file = open(os.getcwd() + '/leitor_tab/static/arquivos/example_input_vazio.tab', 'rb')
        response = self.client.post("/importar")

        self.assertEqual(response.context['status'], 400)

    
    def test_upload_revenue (self):
        upload_file = open(os.getcwd() + '/leitor_tab/static/arquivos/example_input.tab', 'rb')
        response = self.client.post("/importar", data={'file_upload': upload_file})

        self.assertEqual(response.context['revenue'], 95)