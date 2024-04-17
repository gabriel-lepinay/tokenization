# Tokenization project

Project

## Project goal

Blablabla

### Prerequis

You need to have Python3 (3.11.2 used) installed.

### Install dependencies

`pip install -r requirements.txt`

### Setup

1 - Start database

```bash
su postgres
psql token_db #(add -s if validation needed for each request of the file (next step))
\i file.sql # in our case createTable.sql
```

You will need an encryption key and a .env file.To generate an encryption key you can run the `main.py` using `-f` argument. For more information check `python main.py -h`

Here is an template of `.env` file:

```json
DBHOST=localhost
DBPORT=5432
DBNAME=dbName
DBUSER=userName     // same as the one in file.sql
DBPASS=1234

// User need select, insert, update privileges on the database
```

### Start script - CLI version

```bash
cd src
python3 main.py -h
```

### Start script - API version

```bash
cd src
uvicorn api:app --reload
```

You can access to a API documentation using `127.0.0.1:8000/docs`

Created in 2024 - Gabriel Lepinay
