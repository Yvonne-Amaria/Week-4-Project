import unittest, sys

sys.path.append('../repo-name')
from main_py_file_name import append

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()