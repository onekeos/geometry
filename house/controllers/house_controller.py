import json

from app import app, db
from models.house_model import House
from services.house_service import hello, create_response
from flask import request, Response, jsonify


@app.route('/')
@app.route('/house', methods=['GET'])
def get_houses() -> Response:
    house = House.query.all()
    return jsonify([i.as_dict() for i in house])


@app.route('/house/<house_id>', methods=['GET', 'PUT'])
def create_update_house(house_id: int):
    house = House.query.get(house_id)
    if request.method == 'GET':
        if house:
            return jsonify(house.as_dict())
        else:
            return create_response(404, 'not found', 'house not found')
    elif request.method == 'PUT':
        data = request.json
        if not {'latitude', 'longitude'} <= data.keys():
            return jsonify(create_response(400, 'bad request', 'latitude/longitude not found in body'))
        for key, value in data.items():
            try:
                if key != 'family_count':
                    data[key] = float(value)
                else:
                    data[key] = int(value)
            except ValueError:
                return create_response(400, 'bad request', f'invalid type for {key}')
        if house:
            house.latitude = data['latitude']
            house.longitude = data['longitude']
            house.family_count = data.get('family_count', house.family_count)

        else:
            house = House(house_id=house_id, latitude=data['latitude'], longitude=data['longitude'],
                          family_count=data.get('family_count', 0))
            db.session.add(house)
        try:
            db.session.commit()
        except Exception as e:
            return create_response(500, 'internal server error', 'there are some problem with database')
        return jsonify(house.as_dict())
