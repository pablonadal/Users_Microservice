import unittest
from app import create_app, db
from dotenv import load_dotenv
from app.models import Users


load_dotenv()

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_user_create(self):
        user = Users(name='test')
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)