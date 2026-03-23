# Me API

## Обзор

Эндпоинты для управления профилем текущего пользователя.

## Эндпоинты

| Метод | Путь | Описание | Auth |
|-------|------|----------|------|
| POST | `/users/me/register` | Регистрация | Нет |
| POST | `/users/me/login` | Вход | Нет |
| POST | `/users/me/password` | Сброс пароля | Нет |
| GET | `/users/me/` | Получить профиль | Да |

## Регистрация

```
POST /users/me/register
Content-Type: application/json

{
  "first_name": "Alex",
  "last_name": "Smith",
  "username": "alex_smith",
  "email": "alex@example.com",
  "password": "MySecurePass123"
}
```

**Ответ 201:**
```json
{
  "status": 201,
  "data": {
    "first_name": "Alex",
    "last_name": "Smith",
    "username": "alex_smith",
    "email": "alex@example.com",
    "access_token": null
  }
}
```

## Вход

```
POST /users/me/login
Content-Type: application/json

{
  "username": "alex_smith",
  "password": "MySecurePass123"
}
```

**Ответ 201:**
```json
{
  "status": 201,
  "data": {
    "username": "alex_smith",
    "email": "alex@example.com",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

## Сброс пароля

```
POST /users/me/password
Content-Type: application/json

{
  "username": "alex_smith",
  "password": "NewPassword456"
}
```

## Профиль

```
GET /users/me/
Authorization: Bearer <token>
```

**Ответ 200:**
```json
{
  "status": 200,
  "data": {
    "first_name": "Alex",
    "last_name": "Smith",
    "username": "alex_smith",
    "email": "alex@example.com"
  }
}
