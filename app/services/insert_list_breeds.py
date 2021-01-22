from app.models.breed_model import Breed
from app.models import db

import csv
from environs import Env

env = Env()
env.read_env()


def insert_list_csv_breed():

    with open(env('BREEDS_CSV')) as f:

        reader = csv.DictReader(f)
        for breed in reader:
            record = Breed(**{"name": breed['Breed']})
            db.session.add(record)
