from flask import jsonify
from flask_restful import Resource, abort, reqparse, fields, marshal_with

from app import db
from app.models import Vehicle

class VehicleAPI(Resource):
    mfields = {'vid': fields.Integer,
               'vname': fields.String }
    parser = reqparse.RequestParser()
    parser.add_argument('vname', required=True)

    def _get_vehicle(self, vid):
        try:
            vehicle = Vehicle.query.filter_by(vid=vid).one()
        except:
            abort(404, message=f'Vehicle {vid} not exist')
        return vehicle

    @marshal_with(mfields)
    def get(self, vid):
        vehicle = self._get_vehicle(vid)
        return vehicle

    @marshal_with(mfields)
    def post(self):
        arg = self.parser.parse_args()
        new_vehicle = Vehicle(vname=arg['vname'])
        db.session.add(new_vehicle)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return new_vehicle

    @marshal_with(mfields)
    def put(self, vid):
        vehicle = self._get_vehicle(vid)
        arg = self.parser.parse_args()
        vehicle.vname = arg['vname']
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return vehicle

    def delete(self, vid):
        vehicle = self._get_vehicle(vid)
        db.session.delete(vehicle)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return jsonify(status='success', vid=vid)