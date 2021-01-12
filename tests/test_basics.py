import unittest

from app import create_app

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = self.app.test_client() # for HTTP requests

    def tearDown(self):
        self.ctx.pop()

    def test_helloword(self):
        response = self.client.get('/helloworld')
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertEqual(data, 'greeting from cowbon')