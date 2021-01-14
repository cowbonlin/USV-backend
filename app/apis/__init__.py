from abc import ABC, ABCMeta, abstractmethod
from flask import jsonify
from flask.views import MethodViewType
from flask_restful import Resource, abort, marshal_with

from app import db

class MetaAPI(MethodViewType, ABCMeta):
    pass

class BaseAPI(Resource, ABC, metaclass=MetaAPI):
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
            abort(404, 
                  message=f'ID {id} of Model {self._model_class.__tablename__} does not exist')
        return item

    # The reason of wrapping original `get` method is that
    # subclass can't pass mfields variable to @marsh_with decorator
    def get(self, id):
        @marshal_with(self.mfields)
        def _get(self, id):
            return self._get_item(id)
        return _get(self, id)

    def post(self):
        @marshal_with(self.mfields)
        def _post(self):
            new_item = self._model_class(**self.parser.parse_args())
            db.session.add(new_item)
            try:
                db.session.commit()
            except Exception as e:
                print(type(e), e)
                db.session.rollback()
                abort(400, message='Database Error')
            return new_item
        return _post(self)

    def put(self, id):
        @marshal_with(self.mfields)
        def _put(self, id):
            new_item = self._get_item(id)
            for key, value in self.parser.parse_args().items():
                setattr(new_item, key, value)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                abort(400, message='Database Error')
            return new_item
        return _put(self, id)

    def delete(self, id):
        item_to_d = self._get_item(id)
        db.session.delete(item_to_d)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return jsonify(status='success', id=id)


from app.apis import apis

def add_all_resources(api):
    api.add_resource(apis.VehicleAPI, '/vehicle/', '/vehicle/<int:id>')
    api.add_resource(apis.MissionAPI, '/mission/', '/mission/<int:id>')
    api.add_resource(apis.RVehMisAPI, '/rvehmis/', '/rvehmis/<int:id>')
    api.add_resource(apis.AnchorWaypointAPI, '/anchorwaypoint/', '/anchorwaypoint/<int:id>')
    api.add_resource(apis.CommTypeAPI, '/commtype/', '/commtype/<int:id>')