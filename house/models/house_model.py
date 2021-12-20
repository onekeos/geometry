from app import db


class House(db.Model):
    house_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    family_count = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<House {self.house_id}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}