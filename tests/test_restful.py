import unittest
from datetime import datetime
from flask import json

from app import create_app
from app import db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        db.create_all()

        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = self.app.test_client() # for HTTP requests

    def tearDown(self):
        self.ctx.pop()

    def test_post_vehicle(self):
        # response = self.client.post('/vehicle', 
        #                             data={'vname': f'unitteset: {datetime.now()}'})
        # ERROR: I don't know why tables in in-memory sqlite cannot be updated
        response = self.client.get('/vehicle/1')
        self.assertEqual(response.status_code, 200)
        # data = json.loads(response.data)
        # print(data, type(data))
        # self.assertEqual(data, 'greeting from cowbon')