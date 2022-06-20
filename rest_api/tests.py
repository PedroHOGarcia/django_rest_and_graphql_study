from django.test import TestCase, Client
from django.urls import reverse_lazy

# Create your tests here.
class ModelEmploeeTestCase(TestCase):
    def setUp(self) -> None:
        self.new_employee = {
            'name': 'Pedro',
            'department': 'IT',
            'email': 'testcase@testcase.com'
        }
        self.client = Client()


    def test_str_method(self):
        self.assertTrue(str(self.employee), f'{self.employee.name} works in {self.employee.department}')

    
    def test_api_post_user_creation_view(self):
        response = self.client.post(reverse_lazy('rest-api/v1/employee'), data= self.new_employee)
        self.user_id = response.json()['result']['id']
        self.assertTrue(response.status_code, 200)

    
    def test_api_get_user_from_view(self):
        response = self.client.get(reverse_lazy(f'rest-api/v1/employee/{self.user_id}/'))
        self.assertDictEqual(response['result'][0], self.new_employee)


    def test_api_remove_user_view(self):
        response = self.client.delete(reverse_lazy(f'rest-api/v1/employee/{self.user_id}'))
        self.assertEqual(response.status_code, 200)

    
    def test_api_create_user_with_wrong_format(self):
        local_dict = self.new_employee.copy()
        local_dict.pop('name')

        response = self.client.post(reverse_lazy('rest-api/v1/employee'), data= local_dict)
        
        self.assertFalse(response, 200)
