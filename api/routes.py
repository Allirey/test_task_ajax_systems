from flask import jsonify, request
from api import app
from .db_utils import add_test_result, remove_test_result, get_stats


@app.route('/api_v1/test_result/', methods=['POST'])
@app.route('/api_v1/test_result/<int:record_id>', methods=['DELETE'])
def test_result(record_id=None):
    if record_id:
        if request.method == 'DELETE':
            if remove_test_result(record_id):
                return jsonify({'message': 'deleted'}), 204
            else:
                return jsonify({'message': 'not found'}), 404
    else:
        if request.method == 'POST':
            data = request.get_json()

            if add_test_result(data['device_type'], data['operator'], data['success']):
                return jsonify({'message': 'created'}), 201
            else:
                return jsonify({'message': 'bad request'}), 400


@app.route('/api_v1/stat/', methods=['GET'])
def stat():
    stats = get_stats(request.args.get('operator'))
    return jsonify(stats)
