# Pontos da API
Os pontos protegidos só podem ser acessados se o token de acesso for passado no header da requisição.

## /api/users/register
Só aceita **POST**. O request body deve conter (dentro dos parêntesis estão os nomes das keys do formulário):
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

# Para rodar o projeto
abra o terminal e rode os seguintes comendos:

docker build -t comer_bem https://github.com/Paulo-Vinicius-m/2save.git#main
docker run -p 8000:8000 comer_bem

Após isso é só abrir 127.0.0.1:8000/register no navegador e se cadastrar! (os templates html ainda não conseguem realizar autenticação e autorização adequadamente. Para explorar a API de verdade é necessário usar o Postman)

