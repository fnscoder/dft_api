from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Shoe


class ShoeModelTest(TestCase):
    def setUp(self):
        self.obj = Shoe(
            brand='nike',
            color='white',
            size=40,
            price=199.90,
            quantity=5,
        )
        self.obj.save()

    def test_create(self):
        """Shoe object must exist"""
        self.assertTrue(Shoe.objects.exists())

    def test_created_at(self):
        """Shoe must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        """str method must returns shoe's brand"""
        self.assertEqual('nike', str(self.obj))
