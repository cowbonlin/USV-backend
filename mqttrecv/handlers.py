from json import loads

from requests import post
from sqlalchemy.exc import DBAPIError

from database.models import VehState, VehStatsAnchor, RVehStateEncounter

FILENAME_START = 256
IMG_SIZE_START = 16
IMG_SIZE_END = FILENAME_START + IMG_SIZE_START


def handle_image(session, payload):
    # Get file_name and img_size
    file_name = payload[:FILENAME_START].rstrip(b'\x00').decode()
    img_size = int(payload[FILENAME_START:IMG_SIZE_END].rstrip(b'\x00'))
    if img_size != len(payload[IMG_SIZE_END:]):
        print(f'ERR: img_size {img_size} != '
              f'payload size {len(payload[IMG_SIZE_END:])}')

    # Save the file
    with open(f'images/{file_name}', 'wb') as image:
        image.write(payload[FILENAME_START+IMG_SIZE_START:])
    print(f'Saved file {file_name} successfully')


def handle_mytopic(session, payload):
    response = post('http://web:8000/mqtt-record',
                    {"topic": 'mytopic', "payload": payload})
    print("RES:", response)


def create_veh_state(session, payload):
    try:
        veh_state = VehState(**loads(payload))
        session.add(veh_state)
        session.commit()
    except TypeError as e:
        print("ERR:", e)
        return
    except DBAPIError as e:
        print("ERR:", e.orig)
        session.rollback()
        return


def create_vehstats_anchor(session, payload):
    try:
        vehstates_anchor = VehStatsAnchor(**loads(payload))
        session.add(vehstates_anchor)
        session.commit()
    except TypeError as e:
        print("ERR:", e)
        return
    except DBAPIError as e:
        print("ERR:", e.orig)
        session.rollback()
        return


def create_rvse(session, payload):
    try:
        rvse = RVehStateEncounter(**loads(payload))
        session.add(rvse)
        session.commit()
    except TypeError as e:
        print("ERR:", e)
        return
    except DBAPIError as e:
        print("ERR:", e.orig)
        session.rollback()
        return
