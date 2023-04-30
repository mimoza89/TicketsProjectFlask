from models import RoleType, Concert
from tests.base import TestRESTAPIBase, generate_token
from tests.factory import UserFactory, ConcertFactory, get_concert_id


class TestConcertSchema(TestRESTAPIBase):
    def test_required_fields_missing_data_raises(self):
        user = UserFactory(role=RoleType.host)
        token = generate_token(user)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        data = {}

        res = self.client.post("/concerts", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == {
            "message": {
                "title": ["Missing data for required field."],
                "city": ["Missing data for required field."],
                "artist": ["Missing data for required field."],
                "price": ["Missing data for required field."]
            }
        }

    def test_price_under_5_raises(self):
        user = UserFactory(role=RoleType.host)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        data = {
            "title": "Best of",
            "city": "Sofia",
            "artist": "Eros Ramazzotti",
            "price": "4.00"
        }

        res = self.client.post("/concerts", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == {
            "message": {
                "price": ["Must be greater than or equal to 5.0."]
            }
        }
    def test_create_a_concert(self):
        user = UserFactory(role=RoleType.host)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        data = {
            "title": "Best of",
            "city": "Sofia",
            "artist": "Eros Ramazzotti",
            "price": "15.00"
        }

        res = self.client.post("/concerts", headers=headers, json=data)

        concerts = Concert.query.filter_by(hosted_by=user.id).all()
        concert = Concert.query.filter_by(hosted_by=user.id).first()


        assert res.status_code == 201
        assert len(concerts) == 1
        assert concert.city != "Varna"

    def test_edit_a_concert(self):
        user = UserFactory(role=RoleType.host)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        id = get_concert_id

        data = {
            "id": id,
            "title": "Best of",
            "city": "Sofia",
            "artist": "Eros Ramazzotti",
            "price": "15.00"
        }

        res = self.client.put(f"/concert/{id}/edit", headers=headers, json=data)

        concerts = Concert.query.filter_by(hosted_by=user.id).all()
        concert = Concert.query.filter_by(hosted_by=user.id).first()

        assert res.status_code == 201
        assert len(concerts) == 1
        assert concert.city != "Varna"