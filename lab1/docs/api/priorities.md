# Priorities API

## Обзор

Управление приоритетами задач.

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | `/priorities` | Создать приоритет |
| GET | `/priorities` | Список приоритетов |
| GET | `/priorities/{id}` | Приоритет по ID |
| PATCH | `/priorities/{id}` | Обновить |
| DELETE | `/priorities/{id}` | Удалить |

## Модель данных

```json
{
  "name": "Высокий"
}
```

## Примеры

### Создание

```
POST /priorities
Content-Type: application/json

{
  "name": "Средний"
}
```

**Ответ 201:**
```json
{
  "status": 201,
  "data": {
    "id": 1,
    "name": "Средний"
  }
}
```

### Список

```
GET /priorities
```

**Ответ:**
```json
[
  {"id": 1, "name": "Низкий"},
  {"id": 2, "name": "Средний"},
  {"id": 3, "name": "Высокий"}
]
