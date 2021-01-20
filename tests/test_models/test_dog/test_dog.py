from app.models.dog_model import Dog


dog_test = {
    "name": "Fredy",
    "details": "teste teste",
    "owner_id": 1,
    "breed_id": 1,
    "gender": True
}


def test_create_new_Dog_model():
    """ Test if Dog model is creating the right keys """
    dog = Dog(**dog_test)

    for key in dog_test.keys():
        assert dog.__dict__[key] == dog_test[key]


def test_if_photos_relationship_exist():
    dog = Dog(**dog_test)

    assert dog.photos == []


def test_if_breed_relationship_exist():
    dog = Dog(**dog_test)

    assert dog.breed is None


def test_if_interest_relationship_exist():
    dog = Dog(**dog_test)

    assert dog.interest == []


def test_if_conversations_relationship_exist():
    dog = Dog(**dog_test)

    assert dog.conversations == []


def test_if_messages_relationship_exist():
    dog = Dog(**dog_test)

    assert dog.messages == []
