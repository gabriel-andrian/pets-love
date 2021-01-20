# Projeto Conclusao Q3 - Kenzie Academy
## jan/2020
## **Equipe**:
Atauã Pinali Doederlein - Scrum Marter
Cassiano Bitencourt da Silva Doederlein - QA
Eduardo Fior Graminho - PO
Gabriel Vieira Andrian - Tech Leader


[figma](https://www.figma.com/file/rKhKJDDXjixbEJh4NdaMNN/Untitled?node-id=0%3A1)


[database](https://my.vertabelo.com/doc/Py5sWzjnazCGN4antp0BbUdXuRYaUYvx)


[trello](https://trello.com/invite/b/2qOYwJBo/61481b1064c194a986e8ffce92488db3/template-kanban)


Exemplos de commits:

- chore: criou,
- refactor: alterou,
- fix: corrigiu algum erro,.

## **EndPoints**

### _Owner_

* Update:
    ```
    PATCH /owner/
    HEADER <Authorization>
    {
        "name": "",
        "surname": "",
        "document": "",
        "email": "",
        "address": "",
        "password": ""
    }
    # Pode-se atualizar qualquer atributo do owner (um atributo ou mais) deixando-os explícitos no corpo da requisição
    ```

* Delete:
    ```
    DELETE /owner/
    HEADER <Authorization>
    ```

### Like

* Create:
    ```
    POST /like
    HEADER <Authorization>
    {
        "dog_id_give": 0,
        "dog_id_receive": 0,
        "dislike": false
    }
    ```

* Has Like (?):
    ```
    GET /like/dog/<dog_id>/has_like_with/<other_dog_id>
    HEADER <Authorization>
    ```

## Conversations & Messages
### fluxo:
- criar conversation --> pegar id
- criar message --> informar id da conversation

### Conversations:
* New Conversation:
    ```
    POST /conversation
    HEADER <Authorization>

    {
        "dog_id": 0, --> dog que inicia a conversa
        "gog_to": 1, --> dog com quem se vai conversar
    }
    ```
* Get All Conversations (from one dog):
    ```
    GET /conversation/
    HEADER <Authorization>

    {
        "dog_id": 0
    }
    ```

* Get One Conversation (from one dog):
    ```
    GET /conversation/<int:conv_id>
    HEADER <Authorization>

    {
        "dog_id": 0
    }
    ```
### Messages:
* New Message:
    ```
    POST /msg
    HEADER <Authorization>

    {
        "dog_id": 0,
        "message_text" = "Text",
        "conv_id": 0
    }
    ```
* Get Message:
    ```
    GET /msg/<int:msg_id>
    HEADER <Authorization>
    ```

* Delete Message:
    ```
    DELETE /msg/<int:msg_id>
    HEADER <Authorization>

    {
        "dog_id": 0,
        "msg_id": 0
    }
    ```

### Breed

* Listar todas as racas de caes:
    ```
    GET /breed
    HEADER <Authorization>

    ```
