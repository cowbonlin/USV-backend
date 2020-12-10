from . import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    vid = db.Column(db.Integer, unique=True)
    vname = db.Column(db.String(32))


class Mission(db.Model):
    __tablename__ = 'mission'
    id = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer, unique=True)
    mname = db.Column(db.String(32))