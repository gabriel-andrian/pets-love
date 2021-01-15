from app.models import db, ma


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=True)
    document = db.Column(db.String(20), nullable=False, unique=True)
    # cpf, rg, etc.
    email = db.Column(db.String(128), nullable=False, unique=True)
    address = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<Owner {self.name} {self.surname} />"


class OwnerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Owner

    id = ma.auto_field()
    name = ma.auto_field()
    surname = ma.auto_field()
    document = ma.auto_field()
    email = ma.auto_field()
    address = ma.auto_field()
    password = ma.auto_field()
