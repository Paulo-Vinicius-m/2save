# mockup
https://www.figma.com/design/AndxMt8yxIANqOHPPgoIdm/Appetit?node-id=24-370&t=1IAGZ5TfVU2uYNcX-0

# Pontos da API

### Documentação do Endpoint `/api/users/register`

#### Descrição
Este endpoint permite que novos usuários se registrem na plataforma.

#### URL
`/api/users/register`

#### Método HTTP
- POST

#### Corpo da Requisição (JSON)
```json
{
    "username": "Nome de usuário",
    "email1": "email@exemplo.com",
    "email2": "email@exemplo.com",
    "descricao": "Descrição do usuário (opcional para consumidores)",
    "pix": "Chave PIX (opcional para consumidores)",
    "password": "Senha",
    "tipo": "Tipo de usuário (R para Restaurante, C para Consumidor)",
    "identificador": "CNPJ ou CPF",
    "endereco": "Endereço do usuário",
    "imagem": "URL do logo (opcional)"
}
```

#### Respostas
- `201 Created`: Retorna os dados do usuário criado em formato JSON, incluindo um token de autenticação.
- `400 Bad Request`: Se os dados fornecidos forem inválidos ou o tipo de usuário for inválido.

#### Exemplo de Resposta (JSON)
Se for um restaurante:
```json
{
    "username": "self.username",
    "id": "self.id",
    "cnpj": "self.cnpj",
    "email": "self.email",
    "telefone": "self.telefone",
    "imagem": "self.imagem.url if self.imagem else None",
    "endereco": "self.endereco",
    "descricao": "self.descricao",
    "pix": "self.pix",
    "pratos": "produto_serializer(Produto.objects.filter(restaurante=self, tipo='prato'))",
    "bebidas": "produto_serializer(Produto.objects.filter(restaurante=self, tipo='bebida'))"
}
```

Se for um consumidor:
```json
{
    "nome": "self.username",
    "id": "self.id",
    "cpf": "self.cpf",
    "email": "self.email",
    "telefone": "self.telefone",
    "endereco": "self.endereco"
}
```

#### Exemplo de Cabeçalho de Resposta
```http
Set-Cookie: Authorization=<token>; HttpOnly; SameSite=Strict
```

#### Notas
- O token de autenticação também é definido como um cookie `Authorization` com as flags `HttpOnly` e `SameSite=Strict` para segurança adicional.

### Documentação do Endpoint `/api/users/login`

#### Descrição
Este endpoint permite que usuários autenticados façam login na plataforma.

#### URL
`/api/users/login`

#### Método HTTP
- 

POST



#### Corpo da Requisição (JSON)
```json
{
    "email": "email@exemplo.com",
    "password": "Senha"
}
```

#### Respostas
- `200 OK`: Retorna uma mensagem de sucesso, um token de autenticação e os dados do usuário em formato JSON.
- `401 Unauthorized`: Se as credenciais fornecidas forem inválidas.
- `405 Method Not Allowed`: Se o método HTTP utilizado não for 

POST

.

#### Exemplo de Resposta (JSON)
```json
{
    "message": "User authenticated",
    "token": "Token de autenticação",
    "user": {
        "id": 1,
        "name": "Nome de usuário",
        "email": "email@exemplo.com",
        "tipo": "Tipo de usuário",
        "endereco": "Endereço do usuário"
        ... // E mais campos se for um restaurante
    }
}
```

#### Exemplo de Cabeçalho de Resposta
```http
Set-Cookie: Authorization=<token>; HttpOnly; SameSite=Strict
```

#### Notas
- O token de autenticação também é definido como um cookie `Authorization` com as flags `HttpOnly` e `SameSite=Strict` para segurança adicional.

### Documentação do Endpoint `/api/restaurantes`

#### Descrição
Este endpoint permite que os usuários busquem e atualizem informações de restaurantes.

#### URL
`/api/restaurantes`

#### Métodos HTTP
- `GET`
- `PUT`

#### Autenticação
Este endpoint requer autenticação. O token de autenticação deve estar no cookie "Authorization".

### `GET /api/restaurantes`
#### Descrição
Busca informações de restaurantes por nome ou ID. Só é necessário passar uma das duas opções de filtragem.

#### Corpo da Requisição (JSON)
```json
{
    "username": "Nome do restaurante",
    "id": "ID do restaurante"
}
```

#### Respostas
- `200 OK`: Retorna os dados do(s) restaurante(s) em formato JSON.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
Para busca por ID:
```json
{
    "id": 1,
    "username": "Nome do restaurante",
    "email": "email@restaurante.com",
    "cnpj": "00.000.000/0000-00",
    "telefone": "(00) 0000-0000",
    "endereco": "Endereço",
    "imagem": "Número",
    "pix": "pix",
    "descricao": "descrição do restaurante",
}
```

Para busca por nome:
```json
[
    {
        "id": 1,
        "username": "Nome do restaurante",
        "email": "email@restaurante.com",
        "cnpj": "00.000.000/0000-00",
        "telefone": "(00) 0000-0000",
        "endereco": "Endereço",
        "imagem": "Número",
        "pix": "pix",
        "descricao": "descrição do restaurante",
    },
    ...
]
```

### Documentação do Endpoint `/api/alterar-cardapio`

#### Descrição
Este endpoint permite que restaurantes criem, atualizem e deletem os produtos de seu cardápio.

#### URL
`/api/alterar-cardapio`

#### Métodos HTTP
- `POST`
- `PUT`
- `DELETE`

#### Autenticação
Este endpoint requer autenticação com permissão de 'restaurant'. O token de autenticação deve estar presente no cookie "Authorization".

### 

#### POST /api/alterar-cardapio


##### Descrição
Cria um novo produto associado ao restaurante.

##### Corpo da Requisição (JSON)
```json
{
    "nome": "Nome do produto",
    "descricao": "Descrição do produto",
    "preco": "Preço do produto",
    "imagem": "URL da imagem do produto",
    "tipo": "Tipo do produto"
}
```

#### Respostas
- `201 Created`: Retorna os dados do produto criado em formato JSON.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
{
    "id": 1,
    "nome": "Nome do produto",
    "descricao": "Descrição do produto",
    "preco": "Preço do produto",
    "imagem": "URL da imagem do produto",
    "tipo": "Tipo do produto",
}
```

### `PUT /api/alterar-cardapio`
#### Descrição
Atualiza um produto existente.

#### Corpo da Requisição (JSON)
```json
{
    "id": "ID do produto",
    "nome": "Nome do produto",
    "descricao": "Descrição do produto",
    "preco": "Preço do produto",
    "imagem": "URL da imagem do produto",
    "tipo": "Tipo do produto"
}
```

#### Respostas
- `200 OK`: Retorna os dados do produto atualizado em formato JSON.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
{
    "id": 1,
    "nome": "Nome do produto",
    "descricao": "Descrição do produto",
    "preco": "Preço do produto",
    "imagem": "URL da imagem do produto",
    "tipo": "Tipo do produto",
}
```

### `DELETE /api/alterar-cardapio`
#### Descrição
Deleta um produto existente.

#### Corpo da Requisição (JSON)
```json
{
    "id": "ID do produto"
}
```

#### Respostas
- `200 OK`: Confirma que o produto foi deletado.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta
```
200 OK
Produto deletado
```

### Documentação do Endpoint `/api/carrinho`

#### Descrição
Este endpoint permite que os consumidores visualizem e modifiquem o carrinho de compras.

#### URL
`/api/carrinho`

#### Métodos HTTP
- `GET`
- `POST`

#### Autenticação
Este endpoint requer autenticação com permissão de 'customer'. O token de autenticação deve estar no cookie "Authorization"

### `GET /api/carrinho`
#### Descrição
Busca o carrinho de compras do consumidor autenticado.

#### Respostas
- `200 OK`: Retorna os dados do carrinho em formato JSON.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
{
    "id": "ID do carrinho",
    "consumidor": "ID do consumidor",
    "restaurante": "ID do restaurante",
    "produtos": [
        {
            "id": "ID do produto",
            "nome": "Nome do produto",
            "descricao": "Descrição do produto",
            "preco": "Preço do produto",
            "imagem": "URL da imagem do produto",
            "tipo": "Tipo do produto"
        },
        ...
    ]
}
```

### `POST /api/carrinho`
#### Descrição
Adiciona um produto ao carrinho do consumidor autenticado.

#### Corpo da Requisição (JSON)
```json
{
    "produtos": [
        {
            "id": "ID do produto",
            "quantidade": 2
        },
        ...
    ]
}
```
P.S.: A função de quantidade ainda não foi implementada, por hora, o servidor ignora essa informação completamente

#### Respostas
- `200 OK`: Retorna os dados atualizados do carrinho em formato JSON.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
{
    "id": "ID do carrinho",
    "consumidor": "ID do consumidor",
    "restaurante": "ID do restaurante",
    "produtos": [
        {
            "id": "ID do produto",
            "nome": "Nome do produto",
            "descricao": "Descrição do produto",
            "preco": "Preço do produto",
            "imagem": "URL da imagem do produto",
            "tipo": "Tipo do produto"
        },
        ...
    ]
}
```

### `PUT /api/carrinho`
#### Descrição
Atualiza o carrinho do consumidor autenticado, substituindo os produtos existentes pelos novos produtos fornecidos.

#### Corpo da Requisição (JSON)
```json
{
    "produtos": [
        {
            "id": "ID do produto",
            "quantidade": 5
        },
        ...
    ]
}
```

#### Respostas
- `200 OK`: Retorna os dados atualizados do carrinho em formato JSON.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
{
    "id": 1,
    "consumidor": "ID do consumidor",
    "restaurante": "ID do restaurante",
    "produtos": [
        {
            "id": 1,
            "nome": "Nome do produto",
            "descricao": "Descrição do produto",
            "preco": "Preço do produto",
            "imagem": "URL da imagem do produto",
            "tipo": "Tipo do produto"
        },
        ...
    ]
}
```

### Documentação do Endpoint `/api/restaurante/pedidos`

#### Descrição
Este endpoint permite que restaurantes visualizem e atualizem os pedidos recebidos.

#### URL
`/api/restaurante/pedidos`

#### Métodos HTTP
- `GET`
- `PATCH`

#### Autenticação
Este endpoint requer autenticação com permissão de 'restaurant'. O token de autenticação deve estar presente no cookie "Authorization".

### `GET /api/restaurante/pedidos`
#### Descrição
Busca todos os pedidos recebidos pelo restaurante autenticado.

#### Respostas
- `200 OK`: Retorna os dados dos pedidos em formato JSON.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
[
    {
        "id": 1,
        "consumidor": "ID do consumidor",
        "restaurante": "ID do restaurante",
        "produtos": [
            {
                "id": 1,
                "nome": "Nome do produto",
                "descricao": "Descrição do produto",
                "preco": "Preço do produto",
                "imagem": "URL da imagem do produto",
                "tipo": "Tipo do produto"
            },
            ...
        ],
        "aceito": true,
        "entregue": false,
        "data": "2025-01-19T22:34:10.619Z"
    },
    ...
]
```

### `PATCH /api/restaurante/pedidos`
#### Descrição
Atualiza o status de um pedido específico. O corpo da requisição deve conter o ID do pedido a ser alterado. Os novos valores dos campos 'aceito' e 'entregue' são opcionais.

#### Corpo da Requisição (JSON)
```json
{
    "id": "ID do pedido",
    "aceito": true,
    "entregue": false
}
```

#### Respostas
- `200 OK`: Retorna os dados atualizados do pedido em formato JSON.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
{
    "id": "ID do pedido",
    "consumidor": "ID do consumidor",
    "restaurante": "ID do restaurante",
    "produtos": [
        {
            "id": 1,
            "nome": "Nome do produto",
            "descricao": "Descrição do produto",
            "preco": "Preço do produto",
            "imagem": "URL da imagem do produto",
            "tipo": "Tipo do produto"
        },
        ...
    ],
    "aceito": true,
    "entregue": false,
    "data": "2025-01-19T22:34:22.657Z"
}
```

### Documentação do Endpoint `/api/customer/pedidos`

#### Descrição
Este endpoint permite que os consumidores visualizem e criem pedidos.

#### URL
`/api/customer/pedidos`

#### Métodos HTTP
- `GET`
- `POST`

#### Autenticação
Este endpoint requer autenticação com permissão de 'customer'. O token de autenticação deve estar presente no cookie "Authorization".

### `GET /api/customer/pedidos`
#### Descrição
Busca todos os pedidos feitos pelo consumidor autenticado.

#### Respostas
- `200 OK`: Retorna os dados dos pedidos em formato JSON.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
[
    {
        "id": "ID do pedido",
        "consumidor": "ID do consumidor",
        "restaurante": "ID do restaurante",
        "produtos": [
            {
                "id": 1,
                "nome": "Nome do produto",
                "descricao": "Descrição do produto",
                "preco": "Preço do produto",
                "imagem": "URL da imagem do produto",
                "tipo": "Tipo do produto"
            },
            ...
        ],
        "aceito": true,
        "entregue": false,
        "data": "2025-01-19T22:30:44.927Z"
    },
    ...
]
```

### `POST /api/customer/pedidos`
#### Descrição
Cria um novo pedido para o consumidor autenticado.

#### Corpo da Requisição (JSON)
```json
{
    "produtos": [
        {
            "id": "ID do produto",
            "quantidade": 3
        },
        ...
    ]
}
```

#### Respostas
- `201 Created`: Retorna os dados do pedido criado em formato JSON.
- `400 Bad Request`: Se os dados fornecidos forem inválidos.
- `401 Unauthorized`: Se a autenticação falhar ou o usuário não tiver permissão.

#### Exemplo de Resposta (JSON)
```json
{
    "id": "ID do pedido",
    "consumidor": "ID do consumidor",
    "restaurante": "ID do restaurante",
    "produtos": [
        {
            "id": 1,
            "nome": "Nome do produto",
            "descricao": "Descrição do produto",
            "preco": "Preço do produto",
            "imagem": "URL da imagem do produto",
            "tipo": "Tipo do produto"
        },
        ...
    ],
    "aceito": false,
    "entregue": false,
    "data_criacao": "2025-01-19T22:52:42.596Z"
}
```


# Para rodar o projeto
abra o terminal e rode os seguintes comendos:

docker build -t comer_bem https://github.com/Paulo-Vinicius-m/2save.git#main
docker run -p 8000:8000 comer_bem

Após isso é só abrir 127.0.0.1:8000/register no navegador e se cadastrar! (os templates html ainda não conseguem realizar autenticação e autorização adequadamente. Para explorar a API de verdade é necessário usar o Postman)