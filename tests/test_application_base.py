from models import RoleType
from tests.base import TestRESTAPIBase, generate_token
from tests.factory import UserFactory, ConcertFactory


class TestLoginRequired(TestRESTAPIBase):
    def test_login_is_required(self):
        all_guarded_urls = {
            ("POST", "/concerts"),
            ("GET", "/hosts/1/ownconcerts"),
            ("POST", "/purchases"),
            ("PUT", "/concert/1/edit"),
            ("DELETE", "/concert/1/delete"),
            ("GET", "/concert/1/details"),
        }

        for method, url in all_guarded_urls:
            if method == "GET":
                res = self.client.get(url)
            elif method == "POST":
                res = self.client.post(url)
            elif method == "PUT":
                res = self.client.put(url)
            else:
                res = self.client.delete(url)

            assert res.status_code == 401
            assert res.json == {'message': 'Invalid or missing token!'}

class TestAuthorizationRequired(TestRESTAPIBase):
    def test_permission_required_create_a_concert_requires_a_host(self):
        user = UserFactory(role=RoleType.simple_user)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.post("/concerts", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.post("/concerts", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

    def test_permission_required_edit_a_concert_requires_a_host(self):
        user = UserFactory(role=RoleType.simple_user)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        data = {
            "title" : "First title",
            "city" : "First city",
            "artist" : "First artist",
            "price" : 1500
        }

        res = self.client.put("/concert/1/edit", headers=headers, json=data)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        data = {
            "title": "First title",
            "city": "First city",
            "artist": "First artist",
            "price": 1500
        }

        res = self.client.put("/concert/2/edit", headers=headers, json=data)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

    def test_permission_required_view_all_purchases_requires_an_admin(self):
        user = UserFactory(role=RoleType.simple_user)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.get("/allpurchases", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

        user = UserFactory(role=RoleType.host)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.get("/allpurchases", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

    def test_permission_required_view_own_purchases_requires_a_simple_user(self):
        user = UserFactory(role=RoleType.host)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.get("/mypurchases", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.get("/mypurchases", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

    def test_permission_required_delete_a_concert_requires_a_host(self):
        user = UserFactory(role=RoleType.simple_user)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.delete("/concert/1/delete", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}

        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.delete("/concert/2/delete", headers=headers)
        assert res.status_code == 403
        assert res.json == {"message": "You do not have permission to access this resource!"}


