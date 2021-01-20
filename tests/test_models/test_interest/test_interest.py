from app.models.interest_model import Interest


def test_create_interest():
    new_interest = {
        "dog_id": 1,
        "breed_id": 1,
        "gender_interest": True
    }

    interest = Interest(**new_interest)

    for key in new_interest.keys():
        assert interest.__dict__[key] == new_interest[key]
