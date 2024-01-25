from django.test import TestCase
from django.urls import reverse



class ViewTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('aslmovi')

    def test_gets(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert response.json()['message'] == 'aslmovi'
