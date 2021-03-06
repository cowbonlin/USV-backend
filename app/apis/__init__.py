from abc import ABC, ABCMeta, abstractmethod
from flask import jsonify
from flask.views import MethodViewType
from flask_restful import Resource, abort, marshal, marshal_with_field, \
    fields, reqparse

from app import db


def validate_order(arg):
    if arg not in ['asc', 'desc']:
        raise TypeError(f'Invalid Order Arugment "{arg}"')
    return arg


class MetaAPI(MethodViewType, ABCMeta):
    pass


class BaseAPI(Resource, ABC, metaclass=MetaAPI):
    list_parser = reqparse.RequestParser()
    list_parser.add_argument('limit', type=int)
    list_parser.add_argument('sort', type=str)
    list_parser.add_argument('order', type=validate_order, help='asc or desc')

    @property
    @abstractmethod
    def _model_class(self):
        """Model class of Sqlalchemy model defined in app.models"""
        raise NotImplementedError

    @property
    @abstractmethod
    def mfields(self):
        """Marsh fields which define types of response data"""
        raise NotImplementedError

    @property
    @abstractmethod
    def parser(self):
        """Parser for the body of POST and PUT method"""
        raise NotImplementedError

    def _get_item(self, id):
        """Get data queried from database"""
        item = self._model_class.query.get(id)
        if not item:
            abort(400,
                  message=f'{self._model_class.__tablename__}({id}) not exist')
        return item

    def get(self, id=None):
        if id is not None:
            return marshal(self._get_item(id), self.mfields), 200

        @marshal_with_field(fields.List(fields.Nested(self.mfields)))
        def _get_list(self):
            args = self.list_parser.parse_args()
            query = self._model_class.query
            if args['sort']:
                sort = getattr(self._model_class, args['sort'])
                if args['order'] == 'desc':
                    query = query.order_by(sort.desc())
                else:
                    query = query.order_by(sort.asc())
            if args['limit']:
                return query.limit(args['limit'])
            return query.all()
        try:
            return _get_list(self)
        except AttributeError as e:
            abort(400, message=f'{e}')

    def post(self):
        new_item = self._model_class(**self.parser.parse_args())
        db.session.add(new_item)
        try:
            db.session.commit()
        except Exception as e:
            print(type(e), e)
            db.session.rollback()
            abort(400, message=f'Database Error: {e}')
        return marshal(new_item, self.mfields), 201

    def put(self, id):
        new_item = self._get_item(id)
        for key, value in self.parser.parse_args().items():
            setattr(new_item, key, value)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            abort(400, message='Database Error')
        return marshal(new_item, self.mfields), 201

    def delete(self, id):
        item_to_d = self._get_item(id)
        db.session.delete(item_to_d)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            abort(400, message='Database Error')
        return jsonify(status='success', id=id)


class MqttBaseAPI(BaseAPI):
    parser = None

    def post(self):
        abort(405, message='POST method is not allowed within MqttBaseAPI')

    def put(self, id):
        abort(405, message='PUT method is not allowed within MqttBaseAPI')

    def delete(self, id):
        abort(405, message='DELETE method is not allowed within MqttBaseAPI')


from app.apis import apis  # noqa: E402


def add_all_resources(api):
    api.add_resource(apis.VehicleAPI, '/vehicles', '/vehicles/<int:id>')
    api.add_resource(apis.MissionAPI, '/missions', '/missions/<int:id>')
    api.add_resource(apis.RVehMisAPI, '/rvehmiss', '/rvehmiss/<int:id>')
    api.add_resource(apis.AnchorWaypointAPI, '/anchorwaypoints', '/anchorwaypoints/<int:id>')  # noqa: E501
    api.add_resource(apis.UwbModuleAPI, '/uwbmodules', '/uwbmodules/<int:id>', strict_slashes=False)  # noqa: E501
    api.add_resource(apis.RUwbVehAPI, '/ruwbvehs', '/ruwbvehs/<int:id>')
    api.add_resource(apis.RAnchorsAPI, '/ranchors', '/ranchors/<int:id>')
    api.add_resource(apis.CommTypeAPI, '/commtypes', '/commtypes/<int:id>')
    api.add_resource(apis.VehStateAPI, '/vehstates', '/vehstates/<int:id>')
    api.add_resource(apis.VehStatsAnchorAPI, '/vsas', '/vsas/<int:id>')
    api.add_resource(apis.RVehStateEncounterAPI, '/rvses', '/rvses/<int:id>')
