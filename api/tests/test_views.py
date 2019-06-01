from django.contrib.auth.models import User
from django.urls import resolve, reverse

from rest_framework import status
from rest_framework.test import APITestCase

from api import views
from ..models import Shoe


class ShoesTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="dafiti",
            email="dafiti@email.com",
            password="dafitipass",
        )
        url = reverse("api-jwt-auth")
        response = self.client.post(
            url, {"username": "squad5user", "password": "squad5userpass"}, format="json"
        )
        token = response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        shoe_data = {
            "user_id": 1,
            "brand": "nike",
            "color": "white",
            "size": 40,
            "price": 199.90,
            "quantity": 5,
        }

        new_data = {
            "user_id": 1,
            "brand": "adidas",
            "color": "black",
            "size": 42,
            "price": 149.90,
            "quantity": 3,
        }

        partial_data = {
            "quantity": 10,
        }

        self.post_response = self.client.post("/shoes/", shoe_data, format="json")
        self.get_response = self.client.get("/shoes/")
        self.get_one_response = self.client.get("/shoes/1/")
        self.put_response = self.client.put("/shoes/1/", new_data, format="json")
        self.patch_response = self.client.patch("/shoes/1/", partial_data, format="json")
        self.delete_response = self.client.delete("/shoes/1/")

    def test_post_shoes(self):
        self.assertEqual(self.post_response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Shoe.objects.exists())

    def test_get_all_shoes(self):
        self.assertEqual(self.get_response.status_code, status.HTTP_200_OK)

    def test_get_one_shoe(self):
        self.assertEqual(self.get_one_response.status_code, status.HTTP_200_OK)

    def test_put_shoe(self):
        self.assertEqual(self.put_response.status_code, status.HTTP_200_OK)

    def test_patch_shoe(self):
        self.assertEqual(self.patch_response.status_code, status.HTTP_200_OK)

    def test_delete_shoe(self):
        self.assertEqual(self.delete_response.status_code, status.HTTP_200_OK)
