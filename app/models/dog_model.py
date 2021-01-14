from app.models import db


class Dog(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    details = db.Column(db.String(1024), nullable=False)
    owner_id = db.Column(db.Integer, db.foreignKey('owner.id'))
    breed_id = db.Column(db.Integer, db.foreignKey('breed.id'))

    photos = db.relationship("DogPhoto", back_populates="dog_photo")
    give = db.relationship("Like", back_populates="give_b")
    receive = db.relationship("Like", back_populates="receive_b")


class Like(db.model):
    id = db.Column(db.Integer, primary_key=True)
    dog_give_id = db.Column(db.Integer, db.foreignKey('dog.id'))
    dog_receive_id = db.Column(db.Integer, db.foreignKey('dog.id'))

    give_b = db.relationship("Dog", back_populates="give")
    receive_b = db.relationship("Dog", back_populates="receive")


class DogPhoto(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    dog_id = db.Column(db.Integer, db.foreignKey('dog.id'))

    dog_photo = db.relationship("Dog", back_populates="photos")
    # CREATE TABLE dog (
#    id int NOT NULL AUTO_INCREMENT,
#    name varchar(64) NOT NULL,
#    details text NOT NULL,
#    owner_id int NOT NULL,
#    breed_id int NOT NULL,
#    gender bool NOT NULL,
#    CONSTRAINT dog_pk PRIMARY KEY (id)
# );

# id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String, unique=False, nullable=False)
    # surname = db.Column(db.String, unique=False, nullable=True)
    # document = db.Column(db.String(1024), unique=True, nullable=False)
