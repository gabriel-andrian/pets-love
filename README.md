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
    PATCH /owner/<owner_id>
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
    DELETE /owner/<owner_id>
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