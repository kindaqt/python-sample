from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# Database
db = SQLAlchemy()

# Appointment table
class Appointment(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, user_id, start_time):
        self.user_id = user_id
        self.start_time = start_time
        # assign end_time
        self.end_time = start_time + timedelta(minutes=30)
    
from marshmallow import Schema, fields
class AppointmentSchema(Schema):
    id = fields.Integer()
    user_id = fields.String()
    start_time = fields.DateTime()
    end_time = fields.DateTime()