from flask import jsonify


def create_response(code, name, description):
    return jsonify(dict(code=code, name=name, description=description))