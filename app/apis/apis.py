from flask_restful import fields, reqparse

from app.apis import BaseAPI
from app import models


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
               'starttime': fields.DateTime,
               'endtime': fields.DateTime }
    
    #TODO: do validication of datetime arguments
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


class CommTypeAPI(BaseAPI):
    _model_class = models.CommType
    mfields = {'cid': fields.Integer,
               'name': fields.String}
    parser = reqparse.RequestParser()
    parser.add_argument('name')