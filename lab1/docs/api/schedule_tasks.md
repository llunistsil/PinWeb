# Schedule Tasks API

## Обзор

Связь задач с расписанием (многие-ко-многим).

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | `/schedule_tasks/{schedule_id}/{task_id}` | Добавить задачу в расписание |
| GET | `/schedule_tasks` | Все связи |
| GET | `/schedule_tasks/{schedule_id}/{task_id}` | Конкретная связь |
| DELETE | `/schedule_tasks/{schedule_id}/{task_id}` | Удалить связь |

## Модель данных

```json
{
  "schedule_id": 1,
  "task_id": 5,
  "added_at": "2024-01-15T10:00:00"
}
```

## Примеры

### Добавить задачу в расписание

```
POST /schedule_tasks/1/5
```

**Ответ 201:**
```json
{
  "status": 201,
  "data": {
    "schedule_id": 1,
    "task_id": 5,
    "added_at": "2024-01-15T10:00:00"
  }
}
```

### Получить все связи

```
GET /schedule_tasks
```

**Ответ:**
```json
[
  {
    "schedule_id": 1,
    "task_id": 5,
    "added_at": "2024-01-15T10:00:00"
  }
]
```

### Удалить связь

```
DELETE /schedule_tasks/1/5
```

**Ответ:**
```json
{"ok": true}
