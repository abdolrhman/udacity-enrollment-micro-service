from api.core import Mixin
from .base import db
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func


class Enrollment(Mixin, db.Model):

    __tablename__ = "enrollment"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    nanodegree_key = db.Column(db.String, nullable=False)
    udacity_user_key = db.Column(db.String, nullable=False)
    enrolled_at = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.String, default="UNENROLLED")

    def __init__(self, nanodegree_key, ):
        self.nanodegree_key = nanodegree_key
        self.udacity_user_key = "dummy_user"
        self.status = "ENROLLED"

    def __repr__(self):
        return f"<nano-degree-key {self.nanodegree_key}>"
