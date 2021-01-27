from datetime import datetime
from . import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    vid = db.Column(db.Integer, primary_key=True)
    vname = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, default=datetime.now)


class Mission(db.Model):
    __tablename__ = 'mission'
    mid = db.Column(db.Integer, primary_key=True)
    mname = db.Column(db.String(32))
    starttime = db.Column(db.DateTime())
    endtime = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime, default=datetime.now)


class RVehMis(db.Model):
    __tablename__ = 'r_veh_mis'
    rvmid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    vid = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)


class AnchorWaypoint(db.Model):
    __tablename__ = 'anchor_waypoint'
    aid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    globalx = db.Column(db.DECIMAL(11, 9))
    globaly = db.Column(db.DECIMAL(12, 9))
    uwbid = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)


class UwbModule(db.Model):
    __tablename__ = 'uwb_module'
    uwbid = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Binary)
    serial = db.Column(db.Binary)
    created_at = db.Column(db.DateTime, default=datetime.now)
    # usage: u = UwbModule(address=b'\x6a\x25'); print(u.address.hex())


class RUwbVeh(db.Model):
    __tablename__ = 'r_uwb_veh'
    mid = db.Column(db.Integer, primary_key=True)
    vid = db.Column(db.Integer)
    uwbid = db.Column(db.Integer)
    loc = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, default=datetime.now)


class RAnchors(db.Model):
    __tablename__ = 'r_anchors'
    raid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    aid1 = db.Column(db.Integer)
    aid2 = db.Column(db.Integer)
    edge = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now)


class VehState(db.Model):
    __tablename__ = 'vehstate'
    vsid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer)
    vid = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    powerlevel = db.Column(db.Integer)
    tempcpu = db.Column(db.Float)
    tempenv = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now)


class VehStatsAnchor(db.Model):
    __tablename__ = 'vehstats_anchor'
    vsaid = db.Column(db.Integer, primary_key=True)
    vsid = db.Column(db.Integer)
    aid = db.Column(db.Integer)
    commtypeid = db.Column(db.Integer)
    range = db.Column(db.Float)
    rssi = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now)


class RVehStateEncounter(db.Model):
    __tablename__ = 'r_vehstate_encounter'
    rvseid = db.Column(db.Integer, primary_key=True)
    vsid = db.Column(db.Integer)
    vsid2 = db.Column(db.Integer)
    commtypeid = db.Column(db.Integer)
    range = db.Column(db.Float)
    rssi = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now)


class CommType(db.Model):
    __tablename__ = 'commtype'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, default=datetime.now)


class MqttRecord(db.Model):
    __tablename__ = 'mqtt_record'
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(32))
    payload = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now)
