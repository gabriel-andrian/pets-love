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

- Login:
  ```
  POST /auth/login

  {
      "email": "",
      "password": ""
  }
  ```
- Create:
  ```
  POST /auth/signup

  {
      "name": "",
      "surname": "",
      "document": "",
      "email": "",
      "address": "",
      "password": ""
  }
  ```
- Update:
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
- Delete:
  ```
  DELETE /owner/
  HEADER <Authorization>
  ```

### Dog

- Create:

  ```
  POST /dog/
  HEADER <Authorization>
  {
      "name": "",
      "details": "",
      "owner_id": int,
      "breed_id": int,
      "gender": Boolean
  }
  ```

- List All Dogs:

  ```
  GET /dog/
  HEADER <Authorization>
  ```

- By ID:

  ```
  GET /dog/<id>
  HEADER <Authorization>
  ```

- Update:

  ```
  PATCH /dog/<id>
  HEADER <Authorization>
  {
      "name": "",
      "details": "",
      "breed_id": int,
      "gender": ""
  }
  # Pode-se atualizar qualquer atributo do dog (um atributo ou mais menos o owner id) deixando-os explícitos no corpo da requisição.
  # Você tem que ser o owner do dog.
  ```

- Delete:

  ```
  DELETE /dog/<id>
  HEADER <Authorization>

  # Você tem que ser o owner do dog.
  ```

- Match:

  ```
  GET /dog/<id>/matches
  HEADER <Authorization>
  ```

### Photo

- Create:

  ```
  POST /photo/
  HEADER <Authorization>
  {
    "dog_account_id": int,
    "link": ""
  }

  # Só pode adicionar uma foto se você for o owner do dog.
  ```

- Delete:

  ```
  DELETE /photo/<id>
  HEADER <Authorization>

  # Só pode deletar uma foto se você for o owner do dog.
  ```

### Like

- Create:

  ```
  POST /like
  HEADER <Authorization>
  {
        "dog_id_give": 0,
        "dog_id_receive": 0,
        "dislike": false
  }
  ```

- Has Like (?):
  ```
  GET /like/dog/<dog_id>/has_like_with/<other_dog_id>
  HEADER <Authorization>
  ```

## Conversations & Messages

### fluxo:

- criar conversation --> pegar id
- criar message --> informar id da conversation

### Conversations:

- New Conversation:

  ```
  POST /conversation
  HEADER <Authorization>

  {
      "dog_id": 0, --> dog que inicia a conversa
      "gog_to": 1, --> dog com quem se vai conversar
  }
  ```

- Get All Conversations (from one dog):

  ```
  GET /conversation/
  HEADER <Authorization>

  {
      "dog_id": 0
  }
  ```

- Get One Conversation (from one dog):

  ```
  GET /conversation/<int:conv_id>
  HEADER <Authorization>

  {
      "dog_id": 0
  }
  ```

### Messages:

- New Message:

  ```
  POST /msg
  HEADER <Authorization>

  {
      "dog_id": 0,
      "message_text" = "Text",
      "conv_id": 0
  }
  ```

- Get Message:

  ```
  GET /msg/<int:msg_id>
  HEADER <Authorization>
  ```

- Delete Message:

  ```
  DELETE /msg/<int:msg_id>
  HEADER <Authorization>

  {
      "dog_id": 0,
  }
  ```

## Detalhes dos Cãezinhos

### Breed

- Listar todas as raças de caes:

  ```
  GET /breed
  HEADER <Authorization>
  ```

- Adicionar as raças no banco de dados:

  ```
  POST /breed
  HEADER <Authorization>
  ```

### Interest

- Adicionar uma raça e genero de interesse do seu Dog

  ```
  POST /interest/
  HEADER <Authorization>
  ```

- Listar o interesse do Dog selecionado

  ```
  GET /interest/<int: dog_id>
  HEADER <Authorization>
  ```

- Editar a raça e genero de interesse do seu Dog

  ```
  PATCH /interest/<int: dog_id>
  HEADER <Authorization>
  ```
