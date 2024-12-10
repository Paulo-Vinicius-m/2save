# Pontos da API

## /api/users/register
Só aceita **POST**. O request body deve conter:
- username (name)
- email (email)
- confirmação do email (email2)
- tipo de usuário: "R" para restaurante e "C" para consumidor (tipo)
- cpf/cnpj (identificador)

## /api/users/login
Só aceita **POST**. O body deve conter:
- email (email)
- senha (password)

## /api/customer/home
Só aceita **GET**. O body deve conter o nome do restaurante que deseja pesquisar (name)
