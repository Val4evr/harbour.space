# Lecture 07 — Submission

## Deployed API URL

https://api-production-c857.up.railway.app

Swagger docs: https://api-production-c857.up.railway.app/docs

## Entity Description

**Entity:** Book

| Field  | Type    | Description          |
|--------|---------|----------------------|
| id     | integer | Unique ID (auto-generated) |
| title  | string  | Title of the book    |
| author | string  | Author of the book   |
| year   | integer | Year of publication  |

## Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL (Railway managed)
- **Hosting:** Railway

## Proof — curl requests against the live API

### 1. Create a new book (`POST /books`)

```
$ curl -X POST https://api-production-c857.up.railway.app/books \
  -H 'Content-Type: application/json' \
  -d '{"title": "1984", "author": "George Orwell", "year": 1949}'
```

**Response (201):**

```json
{"id": 2, "title": "1984", "author": "George Orwell", "year": 1949}
```

### 2. Get a book by ID (`GET /books/{id}`)

```
$ curl https://api-production-c857.up.railway.app/books/2
```

**Response (200):**

```json
{"id": 2, "title": "1984", "author": "George Orwell", "year": 1949}
```

### 3. List all books (`GET /books`)

```
$ curl https://api-production-c857.up.railway.app/books
```

**Response (200):**

```json
[
  {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
  {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949}
]
```
