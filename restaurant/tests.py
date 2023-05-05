from rest_framework.test import APITestCase
import datetime  


class BasicAuthenticationTest(APITestCase):
    def test_create_restaurant(self):
        data = {
            "username": "test_username",
            "password": "test_password12345"
        }

        self.client.post("/employee/create/", data)
        access_token = self.client.post("/auth/", data).json()["access"]
        headers = {
            "Authorization": "Bearer " + access_token
        }
        data = {
            "title": "Test restaurant"
        }

        response = self.client.post("/restaurant/", data=data, headers=headers)
        self.assertEqual(response.json(), {
                                           "id": 2, 
                                           "title": "Test restaurant", 
                                           "menus": [], 
                                           "created_at": datetime.datetime.now().strftime("%Y-%m-%d"), 
                                           "updated_at": datetime.datetime.now().strftime("%Y-%m-%d")
                                        })
        
    def test_create_menu(self):
        data = {
            "username": "test_username",
            "password": "test_password12345"
        }
        self.client.post("/employee/create/", data)
        access_token = self.client.post("/auth/", data).json()["access"]

        headers = {
            "Authorization": "Bearer " + access_token
        }
        data = {
            "title": "Test restaurant"
        }
        self.client.post("/restaurant/", data=data, headers=headers)
        
        data = {
            "title": "Test menu",
            "weekday": "Monday",
            "restaurant": 1
        }
        response = self.client.post("/restaurant/menu/", data=data, headers=headers)
        self.assertEqual(response.json(), {
                                           "id": 1, 
                                           "title": "Test menu", 
                                           "weekday": "Monday", 
                                           "restaurant": 1,
                                           "votes": 0
                                        })


    
