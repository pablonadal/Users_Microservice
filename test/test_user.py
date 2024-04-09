import unittest
from app import create_app, db
from dotenv import load_dotenv
from app.models import User



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
        user = User(name='test', lastname='test', phone_number='test', email_address='test', password='test')
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertTrue(user.name)
        self.assertTrue(user.lastname)
        self.assertTrue(user.phone_number)
        self.assertTrue(user.email_address)
        self.assertTrue(user.password)

    
    def test_user_read(self):
        user = User(name='test', lastname='test', phone_number='test', email_address='test', password='test')
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertTrue(user.name)
        self.assertTrue(user.lastname)
        self.assertTrue(user.phone_number)
        self.assertTrue(user.email_address)
        self.assertTrue(user.password)

    
    def test_user_find_by_id(self):
        user = User(name='test', lastname='test', phone_number='test', email_address='test', password='test')
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertTrue(user.name)
        user = User.query.get(1)
        self.assertTrue(user)


    def test_user_find_all(self):
        user = User(name='test', lastname='test', phone_number='test', email_address='test', password='test')
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertTrue(user.name)
        users = User.query.all()
        self.assertTrue(users)

    def test_user_update(self):
        user = User(name='test', lastname='test', phone_number='test', email_address='test', password='test')
        db.session.add(user)
        db.session.commit()
        user.name = 'test2'
        db.session.commit()
        self.assertEqual(user.name, 'test2')


    def test_user_delete(self):
        user = User(name='test', lastname='test', phone_number='test', email_address='test', password='test')
        db.session.add(user)
        db.session.commit()
        db.session.delete(user)
        db.session.commit()
        user = User.query.get(1)
        self.assertFalse(user)