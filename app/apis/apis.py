from flask_restful import fields, reqparse

from app.apis import BaseAPI
from app import models


class Hex(fields.Raw):
    def format(self, value):
        return f'0x{value.hex()}'


class VehicleAPI(BaseAPI):
    _model_class = models.Vehicle
    mfields = {'vid': fields.Integer,
               'vname': fields.String}
    parser = reqparse.RequestParser()
    parser.add_argument('vname')


class MissionAPI(BaseAPI):
    _model_class = models.Mission
    mfields = {'mid': fields.Integer,
               'mname': fields.String,
               'starttime': fields.DateTime('iso8601'),
               'endtime': fields.DateTime('iso8601')}

    # TODO: do validication of datetime arguments
    parser = reqparse.RequestParser()
    parser.add_argument('mname')
    parser.add_argument('starttime', help='format: YYYY-MM-DD HH:MM:SS')
    parser.add_argument('endtime', help='format: YYYY-MM-DD HH:MM:SS')


class RVehMisAPI(BaseAPI):
    _model_class = models.RVehMis
    mfields = {'rvmid': fields.Integer,
               'mid': fields.Integer,
               'vid': fields.Integer}
    parser = reqparse.RequestParser()
    parser.add_argument('mid')
    parser.add_argument('vid')


class AnchorWaypointAPI(BaseAPI):
    _model_class = models.AnchorWaypoint
    mfields = {'aid': fields.Integer,
               'mid': fields.Integer,
               'globalx': fields.Fixed(9),
               'globaly': fields.Fixed(9),
               'uwbid': fields.Integer}
    parser = reqparse.RequestParser()
    parser.add_argument('mid')
    parser.add_argument('globalx', help='Deciaml with the precision of 9')
    parser.add_argument('globaly', help='Deciaml with the precision of 9')
    parser.add_argument('uwbid')


class UwbModuleAPI(BaseAPI):
    _model_class = models.UwbModule
    mfields = {'uwbid': fields.Integer,
               'address': Hex,
               'serial': Hex,
               'created_at': fields.DateTime('iso8601')}
    def _hex_to_bytes(s):
        if not s.startswith('0x'):
            raise ValueError('Must start with 0x')
        return bytes.fromhex(s[2:])
    parser = reqparse.RequestParser()
    parser.add_argument('address', type=_hex_to_bytes)
    parser.add_argument('serial', type=_hex_to_bytes)


class RUwbVehAPI(BaseAPI):
    _model_class = models.RUwbVeh
    mfields = {'ruvid': fields.Integer,
               'vid': fields.Integer,
               'uwbid': fields.Integer,
               'loc': fields.String}
    parser = reqparse.RequestParser()
    parser.add_argument('vid', type=int)
    parser.add_argument('uwbid', type=int)
    parser.add_argument('loc', type=str)


class RAnchorsAPI(BaseAPI):
    _model_class = models.RAnchors
    mfields = {'raid': fields.Integer,
               'mid': fields.Integer,
               'aid1': fields.Integer,
               'aid2': fields.Integer,
               'edge': fields.Float}
    parser = reqparse.RequestParser()
    parser.add_argument('mid', type=int)
    parser.add_argument('aid1', type=int)
    parser.add_argument('aid2', type=int)
    parser.add_argument('edge', type=float)


class CommTypeAPI(BaseAPI):
    _model_class = models.CommType
    mfields = {'cid': fields.Integer,
               'name': fields.String}
    parser = reqparse.RequestParser()
    parser.add_argument('name')
