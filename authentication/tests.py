from rest_framework.test import APITestCase


class BasicAuthenticationTest(APITestCase):
    def test_setup(self):
        data = {
            "username": "test_username",
            "password": "test_password12345"
        }
        response = self.client.post("/employee/create/", data)
        self.assertEqual(response.json(), {"username": "test_username"})

    def test_enter_wrong_credentials(self):
        data = {
            "username": "test_username2",
            "password": "test_password123453"
        }
        response = self.client.post("/auth/", data)
        self.assertEqual(response.json()['detail'], "No active account found with the given credentials")

    def test_not_authenticated(self):
        response = self.client.get('/employee/')
        self.assertEqual(response.json()['detail'], "Authentication credentials were not provided.")

    
