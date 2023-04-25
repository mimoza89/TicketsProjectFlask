from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from db import db
from managers.auth import auth
from models.concerts import Concert


class ConcertManager:
    @staticmethod
    def create_a_concert(concert_data):
        current_user = auth.current_user()
        concert_data["hosted_by"] = current_user.id
        concert = Concert(**concert_data)
        db.session.add(concert)
        db.session.commit()
        return concert

    @staticmethod
    def get_all_concerts():
        concerts = Concert.query.filter_by().all()
        return concerts

    @staticmethod
    def edit_concert(pk, data):
        concert = Concert.query.filter_by(id=pk).first()
        if not concert:
            raise BadRequest("Concert with such id does not exist!")

        if concert.hosted_by != auth.current_user().id:
            raise Forbidden("You do not have permission to access this resource!")

        concert.title = data["title"]
        concert.city = data["city"]
        concert.artist = data["artist"]
        concert.price = data["price"]
        db.session.add(concert)
        db.session.commit()
        return concert

    @staticmethod
    def delete_a_concert(pk):
        concert = Concert.query.filter_by(id=pk).first()
        if not concert:
            raise BadRequest("Concert with such id does not exist!")

        if concert.hosted_by != auth.current_user().id:
            raise Forbidden("You do not have permission to access this resource!")

        db.session.delete(concert)
        db.session.commit()
        return (f"The concert {concert.title} of {concert.artist} is deleted successfully!")
