from app.models.like_model import Like


def test_create_like():
    new_like = {
        'dog_id_give': 1,
        'dog_id_receive': 2,
        'dislike': False
    }

    like = Like(**new_like)

    for key in new_like.keys():
        assert like.__dict__[key] == new_like[key]
