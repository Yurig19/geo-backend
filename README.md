# Geo Backend

API backend em Django/DRF para gerenciamento de locais e produtos.

## Tecnologias

- Python 3.10+
- Django 5
- Django REST Framework
- JWT (`djangorestframework-simplejwt`)
- Swagger/OpenAPI (`drf-spectacular`)
- PostgreSQL + PostGIS
- Docker e Docker Compose

## Pré-requisitos

- Python 3.10+ (execução local)
- Docker + Docker Compose (execução em container)
- Arquivo `.env` na raiz do projeto

## Variáveis de ambiente

Use o `.env.example` como base e crie/ajuste o `.env`.

Variáveis principais:

- `DEBUG`
- `SECRET_KEY`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_HOST_DOCKER` (opcional, padrão `db`)
- `DB_PORT_DOCKER` (opcional, padrão `5432`)

## Rodando local (sem Docker para web)

### 1) Subir só o banco com Docker

```bash
docker compose up -d db
```

### 2) Criar ambiente virtual e instalar dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3) Rodar migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 4) Subir a API local

```bash
python3 manage.py runserver
```

API: `http://localhost:8000`  
Docs Swagger: `http://localhost:8000/api/docs/`

## Collection Postman

Collection gerada a partir do Swagger/OpenAPI:

- https://web.postman.co/workspace/My-Workspace~bafdef2c-448e-41af-89ee-3734e798b425/collection/29196134-ee10d885-2d17-4a30-a0a5-0a1896df3c6f?action=share&source=copy-link&creator=29196134

## Importar GeoJSON (uso do solo)

Para os endpoints GIS de `places`, você precisa importar as geometrias de uso do solo antes.

### 1) Coloque o arquivo GeoJSON no projeto

Exemplo recomendado:

- `uso_ocupacao_teste.geojson`

### 2) Execute as migrations

```bash
python3 manage.py migrate
```

### 3) Importe o GeoJSON (execução local)

```bash
venv/bin/python manage.py import_land_use_geojson --path uso_ocupacao_teste.geojson --clear
```

### 4) Importar via Docker (se estiver rodando container `web`)

```bash
docker compose exec web python manage.py import_land_use_geojson --path uso_ocupacao_teste.geojson --clear
```

Observações:

- `--path` aceita caminho relativo (a partir da raiz do projeto) ou absoluto.
- `--clear` apaga os registros atuais de geometrias antes de importar.

## Rotas da API

Base URL: `http://localhost:8000`

Autenticação:

- Rotas protegidas usam `Authorization: Bearer <access_token>`
- Rotas públicas (sem token): login, registro, refresh, schema e docs

### Sistema

| Método | Rota | Auth | Descrição |
|---|---|---|---|
| GET | `/api/schema/` | Não | Schema OpenAPI |
| GET | `/api/docs/` | Não | Swagger UI |
| GET | `/admin/` | Não | Django Admin |

### Auth

| Método | Rota | Auth | Descrição |
|---|---|---|---|
| POST | `/api/auth/register/` | Não | Criar usuário |
| POST | `/api/auth/login/` | Não | Login e retorno de tokens |
| POST | `/api/auth/refresh/` | Não | Renovar access token |
| POST | `/api/token/` | Não | Obter par de tokens JWT |
| POST | `/api/token/refresh/` | Não | Refresh de token JWT |

### Places

| Método | Rota | Auth | Descrição |
|---|---|---|---|
| GET | `/api/places/points/` | Sim | Listar todos os pontos salvos |
| POST | `/api/places/points/` | Sim | Salvar ponto (latitude/longitude) com uso do solo inferido |
| GET | `/api/places/land-uses/` | Sim | Listar possíveis usos do solo |
| GET | `/api/places/land-uses/area/?land_use_description=...` | Sim | Retornar área total (m²) por uso do solo |

### Products

| Método | Rota | Auth | Descrição |
|---|---|---|---|
| GET | `/api/products/` | Sim | Listar produtos |
| POST | `/api/products/` | Sim | Criar produto |
| GET | `/api/products/{product_id}/` | Sim | Buscar produto por ID |
| PUT | `/api/products/{product_id}/` | Sim | Atualizar produto |
| DELETE | `/api/products/{product_id}/` | Sim | Remover produto |
| PATCH | `/api/products/{product_id}/stock/add/` | Sim | Adicionar estoque |
| PATCH | `/api/products/{product_id}/stock/remove/` | Sim | Remover estoque |

### Cash

| Método | Rota | Auth | Descrição |
|---|---|---|---|
| GET | `/api/cash/transactions/` | Sim | Listar todas as transações de caixa |
| POST | `/api/cash/transactions/` | Sim | Registrar movimentação de caixa (INCOME/EXPENSE) |
| GET | `/api/cash/expenses/?type=EXPENSE` | Sim | Listar movimentações por tipo (INCOME ou EXPENSE) |
| GET | `/api/cash/` | Sim | Visualizar resumo do caixa (income, expense, balance) |
  
## Rodando tudo via Docker (web + db)

### 1) Subir containers

```bash
docker compose up -d --build
```

### 2) Rodar migrations no container web

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

API: `http://localhost:8000`  
Docs Swagger: `http://localhost:8000/api/docs/`

## Comandos úteis

### Parar containers

```bash
docker compose down
```

### Resetar banco (apaga volume/dados)

```bash
docker compose down -v
docker compose up -d --build
docker compose exec web python manage.py migrate
```
