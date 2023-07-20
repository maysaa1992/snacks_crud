from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class SnackTest(TestCase):
    def test_list_view_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snacks_list.html')



    def setUp(self):

        self.user=get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='test')

        self.snacks=Snack.objects.create(
            title='test',
            purchaser=self.user,
            description='test' 
        )


    def test_str_method(self):
        self.assertEqual(str(self.snacks),'test')

    def test_detail_view(self):
        url = reverse('snack_detail',args=[self.snacks.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snacks_detail.html')