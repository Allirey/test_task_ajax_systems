from api import db


class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String(64))
    operator = db.Column(db.String(64))
    time = db.Column(db.DateTime)
    success = db.Column(db.Integer)