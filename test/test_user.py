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
    
    def test_user_read(self):
        user = Users(name='test')
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertTrue(user.name)
    
    def test_user_update(self):
        user = Users(name='test')
        db.session.add(user)
        db.session.commit()
        user.name = 'test2'
        db.session.commit()
        self.assertEqual(user.name, 'test2')


    def test_user_delete(client):
        # Crear un usuario de prueba
        user = Users(id=1, name='Test User')
        db.session.add(user)
        db.session.commit()

        # Asegurarse de que el usuario se creó correctamente
        assert Users.query.get(1) is not None

        # Eliminar el usuario
        Users.query.filter_by(id=1).delete()
        db.session.commit()

        # Asegurarse de que el usuario se eliminó correctamente
        assert Users.query.get(1) is None