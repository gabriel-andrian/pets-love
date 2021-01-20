from app.models.photos_model import Photo


photo_test = {
    "dog_account_id": 1,
    "link": "link/photo29"
}


def test_create_all_keys_in_photo():
    """ Test all keys in the new photo model """
    expected = {
        "dog_account_id": 1,
        "link": "link/photo29"
    }
    resp = Photo(**photo_test)

    assert resp.dog_account_id == expected['dog_account_id']
    assert resp.link == expected['link']
