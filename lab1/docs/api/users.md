# Users API

## Обзор

Управление учётными записями пользователей.

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | `/users` | Регистрация |
| GET | `/users` | Список пользователей |
| GET | `/users/{id}` | Профиль по ID |
| PATCH | `/users/{id}` | Обновление |
| DELETE | `/users/{id}` | Удаление |

## Примеры

### Регистрация

```
POST /users
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com"
}
```

**Ответ 201:**
```json
{
  "status": 201,
  "data": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
}
```

### Список пользователей

```
GET /users
```

**Ответ 200:**
```json
[
  {"id": 1, "username": "john_doe", "email": "john@example.com"}
]
```

### Обновление

```
PATCH /users/1
Content-Type: application/json

{
  "first_name": "John"
}
```

### Удаление

```
DELETE /users/1
```

**Ответ 200:**
```json
{"ok": true}
```

## Смежная документация

- [Me API](users/me.md) — текущий пользователь
