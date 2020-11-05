from datetime import datetime
from sqlalchemy import func
from .models import TestResult
from api import db


def add_test_result(device_type, operator, success):
    db.session.add(TestResult(device_type=device_type,
                              operator=operator,
                              time=datetime.now(),
                              success=success))
    db.session.commit()

    return True


def remove_test_result(record_id):
    result = TestResult.query.filter_by(id=record_id).delete()
    db.session.commit()
    return result


def get_stats(operator):
    res = [{'device_type': record.device_type,
            'total_tests': record.total,
            'successes': record.successes,
            'failures': record.total - record.successes
            } for record
           in db.session.query(TestResult.device_type, func.count(TestResult.success).label('total'),
                               func.sum(TestResult.success).label('successes'))
               .filter_by(operator=operator).group_by(TestResult.device_type).all()]

    return res
