import csv
import os
from environs import Env

env = Env()
env.read_env()


def insert_list_breeds_into_table():
    
    with open(env('BREEDS_CSV')) as f:
    reader = csv.DictReader(f)

    reader.to_sql('Breed', con=engine, index= False, if_exists= 'append')
    query = db.update(finaltable).where(finaltable.DataSource == None).values(DataSource == f[i])

    connection.execute(query)