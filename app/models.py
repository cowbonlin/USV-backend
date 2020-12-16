from . import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    vid = db.Column(db.Integer, primary_key=True)
    vname = db.Column(db.String(32))


class Mission(db.Model):
    __tablename__ = 'mission'
    mid = db.Column(db.Integer, primary_key=True)
    mname = db.Column(db.String(32))
    starttime = db.Column(db.DateTime())
    endtime = db.Column(db.DateTime())


class RVehMis(db.Model):
    __tablename__ = 'rvehmis'
    rvmid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    vid = db.Column(db.Integer)


class AnchorWaypoint(db.Model):
    __tablename__ = 'anchorwaypoint'
    aid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    globalx = db.Column(db.DECIMAL(11,9))
    globaly = db.Column(db.DECIMAL(12,9))


class RAnchors(db.Model):
    __tablename__ = 'ranchors'
    raid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    aid1 = db.Column(db.Integer)
    aid2 = db.Column(db.Integer)
    edge = db.Column(db.Float)


class VehState(db.Model):
    __tablename__ = 'vehstate'
    vsid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    vid = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    powerlevel = db.Column(db.Integer)
    tempcpu = db.Column(db.Float)
    tempenv = db.Column(db.Float)


class VehStatsAnchor(db.Model):
    __tablename__ = 'vehstatsanchor'
    vsaid = db.Column(db.Integer, primary_key=True)
    vsid = db.Column(db.Integer)
    aid = db.Column(db.Integer)
    commtype = db.Column(db.String(8))
    range = db.Column(db.Float)
    rssi = db.Column(db.Float)


class RVehStateEncounter(db.Model):
    __tablename__ = 'rvehstateencounter'
    rvseid = db.Column(db.Integer, primary_key=True)
    vsid = db.Column(db.Integer)
    vsid2 = db.Column(db.Integer)
    commtype = db.Column(db.String(8))
    range = db.Column(db.Float)
    rssi = db.Column(db.Float)