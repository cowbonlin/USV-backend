from flask_restful import fields, reqparse
from app.models import Mission
from app.apis import BaseAPI

class MissionAPI(BaseAPI):
    _model_class = Mission
    mfields = {'mid': fields.Integer,
               'mname': fields.String,
               'starttime': fields.DateTime,
               'endtime': fields.DateTime }
    
    #TODO: do validication of datetime arguments
    parser = reqparse.RequestParser()
    parser.add_argument('mname')
    parser.add_argument('starttime', help='format: YYYY-MM-DD HH:MM:SS')
    parser.add_argument('endtime', help='format: YYYY-MM-DD HH:MM:SS')