from json import loads

from requests import post

from database.models import VehState, VehStatsAnchor, RVehStateEncounter


def handle_mytopic(session, payload):
    response = post('http://web:8000/mqtt-record',
                    {"topic": 'mytopic', "payload": payload})
    print("RES:", response)


def create_veh_state(session, payload):
    try:
        veh_state = VehState(**loads(payload))
    except TypeError as e:
        print("ERR:", e)
        return
    session.add(veh_state)
    session.commit()


def create_vehstats_anchor(session, payload):
    try:
        vehstates_anchor = VehStatsAnchor(**loads(payload))
    except TypeError as e:
        print("ERR:", e)
        return
    session.add(vehstates_anchor)
    session.commit()


def create_rvse(session, payload):
    try:
        rvse = RVehStateEncounter(**loads(payload))
    except TypeError as e:
        print("ERR:", e)
        return
    session.add(rvse)
    session.commit()
