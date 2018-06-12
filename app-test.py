from app import app
import os
import unittest

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_database(self):
        tester = os.path.exists("pythonchitter.db")
        self.assertTrue(tester)

class PythonChitterTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test."""
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    def tearDown(self):
        """Destroy blank temp database after each test."""
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def login(self, username, password):
        """Login helper function."""
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)

    def logout(self):
        """Logout helper function."""
        return self.app.get('/logout', follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
