import csv
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config_api import Config

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
db = SQLAlchemy(app)

from .models import TestResult  # import should be here to avoid circular import

db.create_all()

if db.session.query(TestResult).count() == 0:
    print('INSERTING INITIAL DATA')
    with open('test_python.csv') as csvfile:
        init_data = csv.reader(csvfile)

        next(init_data)  # skip header

        for row in init_data:
            device_type = row[0]
            operator = row[1]
            time = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
            success = bool(int(row[3]))

            db.session.add(TestResult(device_type=device_type, operator=operator, time=time, success=success))

db.session.commit()

from . import routes  # import should be here to avoid circular import
