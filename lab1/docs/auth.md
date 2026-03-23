# Аутентификация

## Обзор

Модуль аутентификации обеспечивает безопасность API через JWT-токены и хеширование паролей.

## Компоненты

### Хеширование паролей

```python
get_password_hash(password: str) -> str
verify_password(plain_password: str, hashed_password: str) -> bool
```

### JWT токены

```python
create_access_token(data: str, expiry: timedelta, refresh: bool) -> str
decode_token(token: str) -> dict
```

## Зависимости

| Класс | Назначение |
|-------|------------|
| TokenBearer | Базовая проверка токена |
| AccessTokenBearer | Валидация access токена |

## Алгоритм работы

1. Пользователь регистрируется → пароль хешируется
2. Пользователь входит → создаётся JWT токен
3. Запросы к API → токен передаётся в заголовке
4. Сервер декодирует токен → извлекает данные пользователя
