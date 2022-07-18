import unittest, sys, os

sys.path.append('../flask-example-3')
from hello import app, db

class UsersTests(unittest.TestCase):

    def setup(self):
        app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()


    def register(self, username, email, password):
        return self.app.post('/register',
                            data=dict(username=username,
                                      email=email,
                                      password=password,
                                      confirm_password=password),
                            follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register('test', 'test@example.com', 'FlaskIsAwesome')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()