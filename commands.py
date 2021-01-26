import os
from app import create_app
from app.models import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.cli.command()
def test():
    print('Flask Command: test')
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def create_db():  # with command 'flask create-db'
    print('Flask Command: create-db')
    from app import db
    db.create_all()
