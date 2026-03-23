# Tasks API

## Обзор

Управление задачами пользователей.

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | `/tasks` | Создать задачу |
| GET | `/tasks` | Список задач |
| GET | `/tasks/{id}` | Задача по ID |
| PATCH | `/tasks/{id}` | Обновить задачу |
| DELETE | `/tasks/{id}` | Удалить задачу |

## Модель данных

```json
{
  "description": "Завершить проект",
  "deadline": "2024-02-01T18:00:00",
  "priority_id": 2,
  "user_id": 1
}
```

## Примеры

### Создание задачи

```
POST /tasks
Content-Type: application/json

{
  "description": "Написать документацию",
  "deadline": "2024-01-25T12:00:00",
  "priority_id": 1,
  "user_id": 1
}
```

**Ответ 201:**
```json
{
  "status": 201,
  "data": {
    "id": 10,
    "description": "Написать документацию",
    "deadline": "2024-01-25T12:00:00",
    "priority_id": 1,
    "user_id": 1
  }
}
```

### Список задач

```
GET /tasks
```

**Ответ:**
```json
[
  {
    "id": 1,
    "description": "Сделать рефакторинг",
    "deadline": "2024-01-20T10:00:00",
    "priority_id": 2,
    "user_id": 1
  }
]
```

### Обновление

```
PATCH /tasks/10
Content-Type: application/json

{
  "description": "Обновлённое описание"
}
```

### Удаление

```
DELETE /tasks/10
```

**Ответ:**
```json
{"ok": true}
```

## Смежная документация

- [Priorities API](priorities.md) — приоритеты задач
- [Schedules API](schedules.md) — расписание
- [Time Entries API](time_entries.md) — учёт времени
