## Para Executar

#### Pré-requisitos

1. Possuir o Docker e Docker Compose instalados. [ [Docker](https://docs.docker.com/get-docker/), [Docker Compose](https://docs.docker.com/compose/install/)]
2. Criar o arquivo `.env` no diretório raiz do projeto.
3. Adicionar os valores das variáveis necessárias. Ex.:
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
Acesse: `http://localhost:8000/docs`

## Stack utilizada

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [poetry - Python package e project manager](https://python-poetry.org/)
- [FastApi](https://fastapi.tiangolo.com/)
- [SqlModel](https://sqlmodel.tiangolo.com/)
<!-- - [httpx](https://www.python-httpx.org/) -->
<!-- - [pytest](https://docs.pytest.org/en/stable/) -->

## Referências

- [Design orientado a domínio - DDD](https://lyz-code.github.io/blue-book/architecture/domain_driven_design/)
- [Architecture Patterns with Python](https://www.cosmicpython.com/book/preface.html)
