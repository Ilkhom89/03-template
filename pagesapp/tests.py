from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code,200)

    def test_plat_page_status_code(self):
        response = self.client.get('/platforma/')
        self.assertEqual(response.status_code,200)

    def test_pract_page_status_code(self):
        response = self.client.get('/practikum/')
        self.assertEqual(response.status_code,200)