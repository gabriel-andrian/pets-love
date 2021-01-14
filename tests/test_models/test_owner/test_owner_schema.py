from app.models.owner_model import OwnerSchema, Owner


def test_if_schema_serialize_the_owner_correctly():
    new_owner = {
        'name': "Rodisval",
        'surname': "Pereira",
        'document': "066-666-666-59",
        'email': "rodisval.pereira@maildrop.cc",
        'address': "Rua de Teste, 1",
        'password': "1234"
    }

    owner = Owner(**new_owner)

    serialized_owner = OwnerSchema().dump(owner)

    for key in new_owner.keys():
        assert serialized_owner[key] == new_owner[key]
