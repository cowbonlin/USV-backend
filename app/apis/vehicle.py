from flask_restful import fields, reqparse
from app.apis import BaseAPI
from app.models import Vehicle

class VehicleAPI(BaseAPI):
    _model_class = Vehicle
    mfields = {'vid': fields.Integer,
               'vname': fields.String }
    # for POST and PUT
    parser = reqparse.RequestParser()
    parser.add_argument('vname')