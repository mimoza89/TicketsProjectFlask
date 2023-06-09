from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.purchases import PurchaseManager
from models import RoleType
from schemas.request_schemas.purchases import PurchaseRequestSchema
from schemas.response_schemas.purchases import PurchaseResponseSchema
from utils.decorators import validate_schema, permission_required


class PurchaseResource(Resource):
    @auth.login_required()
    @validate_schema(PurchaseRequestSchema)
    def post(self):
        data = request.get_json()
        purchase = PurchaseManager.make_a_purchase(data)

        return purchase


class OwnPurchasesResource(Resource):
    @auth.login_required()
    @permission_required(RoleType.simple_user)
    def get(self):
        purchases = PurchaseManager.get_own_purchases()
        return PurchaseResponseSchema(many=True).dump(purchases)


class PurchasesResource(Resource):
    @auth.login_required()
    @permission_required(RoleType.admin)
    def get(self):
        purchases = PurchaseManager.get_all_purchases()
        return PurchaseResponseSchema(many=True).dump(purchases)