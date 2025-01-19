# mockup
https://www.figma.com/design/AndxMt8yxIANqOHPPgoIdm/Appetit?node-id=24-370&t=1IAGZ5TfVU2uYNcX-0

# Pontos da API
Os pontos protegidos só podem ser acessados se o token de acesso for passado no header da requisição.

## /api/users/register
Só aceita **POST**. O request body deve conter (dentro dos parênteses estão os nomes das keys do formulário):
- Username (name)
- Email (email)
- Confirmação do email (email2)
- Senha (password)
- Tipo de usuário: "R" para restaurante e "C" para consumidor (tipo)
- cpf/cnpj (identificador)

Retorna um json com o token de acesso.

## /api/users/login
Só aceita **POST**. O request body deve conter:
- Email (email)
- Senha (password)

Retorna um json com o token de acesso.

## /api/customer/home (protegido)
Só aceita **GET**. O body deve conter o nome do restaurante que deseja pesquisar (name)

Retorna um json com os restaurantes que se encaixam na pesquisa.

Paulo-Vinicius-m: Gere uma documentação do endpoint /api/alterar-cardapio (definida pela classe view_produtos) para que os desenvolvedores front end saibam utilizá-lo

Workspace: Collecting workspace information

### Documentação do Endpoint `/api/alterar-cardapio`

#### Descrição
Este endpoint permite que restaurantes criem, atualizem e deletem produtos do cardápio.

#### URL
`/api/alterar-cardapio`

#### Métodos HTTP
- 

POST


- `PUT`
- `DELETE`

#### Autenticação
Este endpoint requer autenticação com permissão de 'restaurant'. O token de autenticação deve ser enviado no cabeçalho da requisição.

#### Exemplo de Cabeçalho de Autenticação
```http
Authorization: Bearer <seu_token_aqui>
```

### 

POST /api/alterar-cardapio


#### Descrição
Cria um novo produto associado a um restaurante.

#### Corpo da Requisição (JSON)
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
    "restaurante": "ID do restaurante"
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
    "restaurante": "ID do restaurante"
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
    "id": 1,
    "consumidor": "ID do consumidor",
    "restaurante": null,
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


# Para rodar o projeto
abra o terminal e rode os seguintes comendos:

docker build -t comer_bem https://github.com/Paulo-Vinicius-m/2save.git#main
docker run -p 8000:8000 comer_bem

Após isso é só abrir 127.0.0.1:8000/register no navegador e se cadastrar! (os templates html ainda não conseguem realizar autenticação e autorização adequadamente. Para explorar a API de verdade é necessário usar o Postman)