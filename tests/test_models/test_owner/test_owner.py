from app.models.owner_model import Owner


def test_if_with_all_props_can_be_created_an_owner():
    new_owner = {
        'name': "Rodisval",
        'surname': "Pereira",
        'document': "066.666.666.59",
        'email': "rodisval.pereira@maildrop.cc",
        'address': "Rua de Teste, 1",
        'password': "1234"
    }

    owner = Owner(**new_owner)

    for key in new_owner.keys():
        assert owner.__dict__[key] == new_owner[key]
