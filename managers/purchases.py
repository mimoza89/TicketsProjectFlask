import stripe
from decouple import config

from db import db
from managers.auth import auth
from models import Purchase
from models.concerts import Concert

stripe.api_key = config('STRIPE_KEY')
class PurchaseManager:
    @staticmethod
    def make_a_purchase(data):
        user = auth.current_user()
        data['user_id'] = user.id
        purchase = Purchase(**data)
        concert = Concert.query.filter_by(id=purchase.concert_id).first()
        amount_to_pay = data['quantity'] * concert.price

        if user.purchased_tickets is None:
            user.purchased_tickets = 0
        user.purchased_tickets += data['quantity']

        try:
            customer = stripe.Customer.create(email=user.email)
            payment_method = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": "4242424242424242",
                    "exp_month": 10,
                    "exp_year": 2035,
                    "cvc": "1457"
                }
            )

            stripe.Customer.list_payment_methods(
                customer.id,
                type="card"
            )


            intent = stripe.PaymentIntent.create(amount=int(amount_to_pay), currency="bgn", payment_method_types=["card"], payment_method=payment_method)
        except Exception as ex:
            return str(ex)

        if intent:
            stripe.PaymentIntent.confirm(intent.id, payment_method="pm_card_visa")
            client_secret = intent.client_secret

        db.session.add(purchase, user)
        db.session.commit()

        return amount_to_pay

    @staticmethod
    def get_own_purchases():
        user = auth.current_user()
        purchases = Purchase.query.filter_by(user_id=user.id).all()
        return purchases

    @staticmethod
    def get_all_purchases():
        purchases = Purchase.query.filter_by().all()
        return purchases