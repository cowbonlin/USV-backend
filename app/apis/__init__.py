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
        raise NotImplementedError

    @property
    @abstractmethod
    def mfields(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def parser(self):
        raise NotImplementedError

    def _get_item(self, id):
        item = self._model_class.query.get(id)
        if not item:
            abort(404, 
                  message=f'ID {id} of Model {self._model_class.__tablename__} does not exist')
        return item

    # The reason of wrapping original get function with @marsh_with deco is that
    # subclass can't pass mfields variable to @marsh_with
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
                print(e)
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


from .vehicle import VehicleAPI
from .mission import MissionAPI

def add_all_resources(api):
    api.add_resource(VehicleAPI, '/vehicle/', '/vehicle/<int:id>')
    api.add_resource(MissionAPI, '/mission/', '/mission/<int:id>')