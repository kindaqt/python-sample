from flask import Flask, request, jsonify
import datetime

from sqlalchemy import func
from models import AppointmentSchema, db
from models import Appointment

app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/appointment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.create_all(app=app)

@app.route('/appointments', methods=['POST'])
def add_appointment():
    content = request.json
    user_id = content['user_id']

    # convert start_time from string to datetime
    start_time = datetime.datetime.strptime(content['start_time'], '%Y-%m-%d %H:%M:%S.%f')

    # return 400 if minute is not on half hour
    if start_time.minute != 0 and start_time.minute != 30:
        return "start_time must be on the half hour", 400

    # query db to prevent multiple appointments from being scheduled on the same day
    if Appointment.query.filter(
        func.date(Appointment.start_time) == start_time.date()
    ).first() is not None:
        return 'only one appointment per day', 400

    db.session.add(Appointment(user_id, start_time))
    db.session.commit()

    return 'success'

@app.route('/appointments', methods=['GET'])
def get_appointment():
    content = request.json

    return jsonify(
        AppointmentSchema(
            many=True, 
            only=("start_time", "end_time")
        ).dump(
            Appointment.query.filter_by(user_id=content['user_id']).all()
        )
    )