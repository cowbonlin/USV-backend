from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Binary, \
    DECIMAL
from database.sa import Base


class Vehicle(Base):
    __tablename__ = 'vehicle'
    vid = Column(Integer, primary_key=True)
    vname = Column(String(32))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class Mission(Base):
    __tablename__ = 'mission'
    mid = Column(Integer, primary_key=True)
    mname = Column(String(32))
    starttime = Column(DateTime())
    endtime = Column(DateTime())
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class RVehMis(Base):
    __tablename__ = 'r_veh_mis'
    rvmid = Column(Integer, primary_key=True)
    mid = Column(Integer)
    vid = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class AnchorWaypoint(Base):
    __tablename__ = 'anchor_waypoint'
    aid = Column(Integer, primary_key=True)
    mid = Column(Integer)
    globalx = Column(DECIMAL(11, 9))
    globaly = Column(DECIMAL(12, 9))
    uwbid = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class UwbModule(Base):
    __tablename__ = 'uwb_module'
    uwbid = Column(Integer, primary_key=True)
    address = Column(Binary)
    serial = Column(Binary)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
    # usage: u = UwbModule(address=b'\x6a\x25'); print(u.address.hex())


class RUwbVeh(Base):
    __tablename__ = 'r_uwb_veh'
    ruvid = Column(Integer, primary_key=True)
    vid = Column(Integer)
    uwbid = Column(Integer)
    loc = Column(String(32))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class RAnchors(Base):
    __tablename__ = 'r_anchors'
    raid = Column(Integer, primary_key=True)
    mid = Column(Integer)
    aid1 = Column(Integer)
    aid2 = Column(Integer)
    edge = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class VehState(Base):
    __tablename__ = 'vehstate'
    vsid = Column(Integer, primary_key=True)
    mid = Column(Integer)
    vid = Column(Integer)
    timestamp = Column(DateTime)
    powerlevel = Column(Integer)
    tempcpu = Column(Float)
    tempenv = Column(Float)
    globalx = Column(DECIMAL(11, 9))
    globaly = Column(DECIMAL(12, 9))
    created_at = Column(DateTime, default=datetime.now)


class VehStatsAnchor(Base):
    __tablename__ = 'vehstats_anchor'
    vsaid = Column(Integer, primary_key=True)
    vsid = Column(Integer)
    aid = Column(Integer)
    commtypeid = Column(Integer)
    range = Column(Float)
    rssi = Column(Float)
    created_at = Column(DateTime, default=datetime.now)


class RVehStateEncounter(Base):
    __tablename__ = 'r_vehstate_encounter'
    rvseid = Column(Integer, primary_key=True)
    vsid = Column(Integer)
    vsid2 = Column(Integer)
    commtypeid = Column(Integer)
    range = Column(Float)
    rssi = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class CommType(Base):
    __tablename__ = 'commtype'
    cid = Column(Integer, primary_key=True)
    name = Column(String(32))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


class MqttRecord(Base):
    __tablename__ = 'mqtt_record'
    id = Column(Integer, primary_key=True)
    topic = Column(String(32))
    payload = Column(String(128))
    created_at = Column(DateTime, default=datetime.now)
