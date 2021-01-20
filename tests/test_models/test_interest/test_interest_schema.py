from app.models.interest_model import Interest, InterestSchema


def test_schema_serialize_interest():
    new_interest = {
        "dog_id": 1,
        "breed_id": 1,
        "gender_interest": True
    }

    interest = Interest(**new_interest)

    interest_schema = InterestSchema().dump(interest)

    for key in new_interest.keys():
        assert interest_schema[key] == new_interest[key]
