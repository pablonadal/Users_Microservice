import unittest
from flask import current_app
from app import create_app
#from app.models import Apartment


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app('')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_app_exists(self):
        self.assertFalse(current_app)