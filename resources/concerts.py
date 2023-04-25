from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.concerts import ConcertManager
from models.concerts import Concert
from models.enums import RoleType
from schemas.request_schemas.concerts import ConcertCreateRequestSchema
from schemas.response_schemas.concerts import ConcertResponseSchema
from utils.decorators import permission_required, validate_schema


class ConcertsResource(Resource):
    @auth.login_required()
    @permission_required(RoleType.host)
    @validate_schema(ConcertCreateRequestSchema)
    def post(self):
        data = request.get_json()
        concert = ConcertManager.create_a_concert(data)
        return ConcertResponseSchema().dump(concert), 201

    def get(self):
        concerts = ConcertManager.get_all_concerts()
        return ConcertResponseSchema(many=True).dump(concerts)


class ConcertResource(Resource):
    @auth.login_required()
    @validate_schema(ConcertCreateRequestSchema)
    @permission_required(RoleType.host)
    def put(self, pk):
        data = request.get_json()
        concert = ConcertManager.edit_concert(pk, data)
        return ConcertResponseSchema().dump(concert)


class ConcertDeleteResource(Resource):
    @auth.login_required()
    @permission_required(RoleType.host)
    def delete(self, pk):
        concert = ConcertManager.delete_a_concert(pk)
        return concert