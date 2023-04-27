from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.purchases import PurchaseManager
from schemas.request_schemas.purchases import PurchaseRequestSchema
from schemas.response_schemas.purchases import PurchaseResponseSchema
from utils.decorators import validate_schema


class PurchaseResource(Resource):
    @auth.login_required()
    @validate_schema(PurchaseRequestSchema)
    def post(self):
        data = request.get_json()
        purchase = PurchaseManager.make_a_purchase(data)

        return purchase


class OwnPurchasesResource(Resource):
    @auth.login_required()
    def get(self):
        purchases = PurchaseManager.get_own_purchases()
        return PurchaseResponseSchema(many=True).dump(purchases)