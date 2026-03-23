# Schedules API

## Обзор

Управление расписанием пользователей.

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | `/schedules` | Создать расписание |
| GET | `/schedules` | Список расписаний |
| GET | `/schedules/{id}` | Расписание по ID |
| PATCH | `/schedules/{id}` | Обновить |
| DELETE | `/schedules/{id}` | Удалить |

## Модель данных

```json
{
  "user_id": 1,
  "date": "2024-01-15T09:00:00"
}
```

## Примеры

### Создание

```
POST /schedules
Content-Type: application/json

{
  "user_id": 1,
  "date": "2024-01-20T10:00:00"
}
```

### Получение списка

```
GET /schedules
```

**Ответ:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "date": "2024-01-20T10:00:00"
  }
]
```

## Смежная документация

- [Schedule Tasks API](schedule_tasks.md) — связь с задачами
