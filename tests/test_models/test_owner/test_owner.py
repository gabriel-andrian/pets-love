from app.models.owner_model import Owner
from app.models.dog_model import Dog

new_owner = {
    'name': "Rodisval",
    'surname': "Pereira",
    'document': "066.666.666.59",
    'email': "rodisval.pereira@maildrop.cc",
    'address': "Rua de Teste, 1",
    'password': "1234"
}

owner = Owner(**new_owner)


def test_if_with_all_props_can_be_created_an_owner():

    for key in new_owner.keys():
        if key != 'password':
            assert owner.__dict__[key] == new_owner[key]


def test_if_owner_can_have_dogs():
    new_dog = {
        "name": "Cachorro",
        "details": "é um cachorro",
        "owner_id": 1,
        "breed_id": 1,
        "gender": False
    }

    dog = Dog(**new_dog)
    owner.dogs.append(dog)

    assert len(owner.dogs) == 1
