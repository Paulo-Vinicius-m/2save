# Pontos da API
Os pontos protegidos só podem ser acessados se o token de acesso for passado no header da requisição.

## /api/users/register
Só aceita **POST**. O request body deve conter:
- Username (name)
- Email (email)
- Confirmação do email (email2)
- Senha (password)
- Tipo de usuário: "R" para restaurante e "C" para consumidor (tipo)
- cpf/cnpj (identificador)

Retorna um json com o token de acesso.

## /api/users/login
Só aceita **POST**. O body deve conter:
- Email (email)
- Senha (password)

Retorna um json com o token de acesso.

## /api/customer/home (protegido)
Só aceita **GET**. O body deve conter o nome do restaurante que deseja pesquisar (name)

Retorna um json com os restaurantes que se encaixam na pesquisa.
