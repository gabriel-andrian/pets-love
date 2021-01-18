from app.models.like_model import Like


def verify_match(like: Like):
    # Se o dislike for --False--, verificar se possui algum like dado a ele
    if not like.dislike:
        # Se sim, verificar se o id do dog dado o like está entre os que deram
        # o like para ele e o dislike for --False--
        like_received = Like.query.filter_by(
            dog_id_receive=like.dog_id_give,
            dog_id_give=like.dog_id_receive,
            dislike=False).first()

        if like_received is not None:
            # Se sim, modificar o match de ambos como --True--
            like.match = True
            like_received.match = True
