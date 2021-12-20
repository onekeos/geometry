import json

from app import app
from models.house_model import House
from services.house_service import hello, create_response
from flask import jsonify, request, Response


@app.route('/')
@app.route('/house', methods=['GET'])
def get_houses() -> Response:
    house = House.query.all()
    return jsonify([i.as_dict() for i in house])


@app.route('/house/<house_id>', methods=['GET', 'PUT'])
def create_update_house(house_id: int):
    if request.method == 'GET':
        house = House.query.get(house_id)
        if house:
            return jsonify(house.as_dict())
        else:
            return jsonify(create_response(404, 'not found', 'house not found'))
    elif request.method == 'PUT':
        data = request.json
        if not {'latitude', 'longitude'} <= data.keys():
            return jsonify(create_response(400, 'bad request', 'latitude/longitude not found in body'))
        return 'Hello World!'
