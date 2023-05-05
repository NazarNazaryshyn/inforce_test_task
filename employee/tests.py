from rest_framework.test import APITestCase


class BasicAuthenticationTest(APITestCase):
    def test_setup(self):
        data = {
            "username": "test_username",
            "password": "test_password12345"
        }
        response = self.client.post("/employee/create/", data)
        self.assertEqual(response.json(), {"username": "test_username"})

    def test_get_all_employees(self):
        data = {
            "username": "test_username",
            "password": "test_password12345"
        }

        self.client.post("/employee/create/", data)
        access_token = self.client.post("/auth/", data).json()["access"]
        headers = {
            "Authorization": "Bearer " + access_token
        }
        response = self.client.get("/employee/", headers=headers)
        self.assertEqual(response.json(), [{"id": 1, "username": "test_username"}])

