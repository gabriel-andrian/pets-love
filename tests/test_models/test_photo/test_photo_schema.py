from app.models.photos_model import Photo, PhotoSchema

photo_test = {
    "dog_account_id": 1,
    "link": "link/photo29"
}


def test_photo_schema_serialize():
    """ Test if photoSchema serialize correctly """
    expected = {
        "id": None,
        "dog_account_id": 1,
        "link": "link/photo29"
    }
    photo = Photo(**photo_test)
    photo_schema = PhotoSchema().dump(photo)

    assert expected == photo_schema
