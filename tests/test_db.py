import unittest

from app import create_app, db
from app.models import Vehicle


class DbTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
        self.client = self.app.test_client()  # for HTTP requests

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_add_schools(self):
        vehicles = Vehicle.query.all()
        print(vehicles)
