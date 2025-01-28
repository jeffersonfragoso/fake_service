# Fake Service

Serviço responsável por **User Purchases** e **Admin Reports**

## Funcionamento

Para possibilitar operar o sistema, durante a inicialização da API, será feito o cadastro de dois usuários, conforme configurado no arquivo de ambiente `.env`.

Um usuário terá o papel **user** e o outro terá o papel **admin**.

Através da rota `[POST] /v1/user` é possível cadastrar itens de **User Purchases**

Através da rota `[POST] /v1/admin` é possível cadastrar itens de **Admin Reports**

Através da rota `[GET] /v1/user` é possível consultar o primeiro **User Purchases** cadastrado.

Através da rota `[GET] /v1/admin` é possível consultar o primeiro **Admin Reports** cadastrado.

As rotas `[GET] /v1/user` e `[GET] /v1/admin` são protegidas, sendo acessível apenas para usuários com o papel **user** e **admin** respoectivamente.

Para utilizar as rotas `[GET] /v1/user` e `[GET] /v1/admin` é necessário informar o header `Authorization: Bearer <token>`.

Através da rota `[POST] /v1/token` é possível obter o token de autenticação conforme credenciais informadas.

Para testar o funcionamento utilize a interface gráfica do Swagger após iniciar a API.

## Para Executar

#### Pré-requisitos

1. Possuir o Docker e Docker Compose instalados. [ [Docker](https://docs.docker.com/get-docker/), [Docker Compose](https://docs.docker.com/compose/install/)]
2. Criar o arquivo `.env` no diretório raiz do projeto.
3. Adicionar no arquivo `.env` os valores das variáveis necessárias. Ex.:
```
DB_URL=sqlite:///database.db
SECRET_KEY=secret_key
DEFAULT_ADMIN=admin
DEFAULT_ADMIN_PASSWORD=JKSipm0YH
DEFAULT_USER=user
DEFAULT_USER_PASSWORD=L0XuwPOdS5U
```

Após atender aos pré-requisitos execute o comando abaixo:

```bash
  $ docker compose up --build --always-recreate-deps
```
Após execução do comando aguarde alguns segundos até ver algo como:

```
api  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
api  | INFO:     Started reloader process [1] using StatReload
api  | INFO:     Started server process [8]
api  | INFO:     Waiting for application startup.
api  | INFO:     Application startup complete.
```
Acesse a interface swagger para testar as requisições: `http://localhost:8000/docs`

## Execução dos testes da aplicação

Para executar os testes utilize o comando abaixo:

```bash
  $ docker compose run --rm --no-deps --entrypoint="python -m pytest -p no:cacheprovider" api
```

## Stack utilizada

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [Poetry - Python package e project manager](https://python-poetry.org/)
- [FastApi](https://fastapi.tiangolo.com/)
- [SqlModel](https://sqlmodel.tiangolo.com/)
- [pytest](https://docs.pytest.org/en/stable/)

## Referências

- [Design orientado a domínio - DDD](https://lyz-code.github.io/blue-book/architecture/domain_driven_design/)
- [Architecture Patterns with Python](https://www.cosmicpython.com/book/preface.html)
