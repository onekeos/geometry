def hello():
    return 'hello world'


def create_response(code, name, description):
    return dict(code=code, name=name, description=description)