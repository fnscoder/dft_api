from django.contrib.auth.models import User
from django.urls import resolve, reverse

from rest_framework import status
from rest_framework.test import APITestCase

from api import views
from ..models import Shoe


class ShoesTest(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username="dafiti",
            email="dafiti@email.com",
            password="dafitipass",
        )
        url = reverse("api-jwt-auth")
        response = self.client.post(
            url, {
                "username": "dafiti", 
                "password": "dafitipass"
            }, 
            format="json"
        )
        token = response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        shoe_data = {
            "brand": "nike",
            "color": "white",
            "size": 40,
            "price": 199.90,
            "quantity": 5,
        }

        new_data = {
            "brand": "adidas",
            "color": "black",
            "size": 42,
            "price": 149.90,
            "quantity": 3,
        }

        partial_data = {
            "quantity": 10,
        }
        
        self.post_response = self.client.post("/api/shoes/", shoe_data, format="json")
        self.get_all_response = self.client.get("/api/shoes/")
        self.get_one_response = self.client.get("/api/shoes/1/")
        self.put_response = self.client.put("/api/shoes/1/", new_data, format="json")
        self.patch_response = self.client.patch("/api/shoes/1/", partial_data, format="json")
        self.delete_response = self.client.delete("/api/shoes/1/")

    def test_post_shoes(self):
        self.assertEqual(self.post_response.status_code, status.HTTP_201_CREATED)

    def test_get_all_shoes(self):
        self.assertEqual(self.get_all_response.status_code, status.HTTP_200_OK)

    def test_pagination_shoes(self):
        contents = ("count",
                    "next",
                    "previous",
                    "results",
                )
        for content in contents:
            with self.subTest():
                self.assertContains(self.get_all_response, content)        

    def test_get_one_shoe(self):
        self.assertEqual(self.get_one_response.status_code, status.HTTP_200_OK)

    def test_put_shoe(self):
        self.assertEqual(self.put_response.status_code, status.HTTP_200_OK)

    def test_patch_shoe(self):
        self.assertEqual(self.patch_response.status_code, status.HTTP_200_OK)

    def test_delete_shoe(self):
        self.assertEqual(self.delete_response.status_code, status.HTTP_204_NO_CONTENT)
