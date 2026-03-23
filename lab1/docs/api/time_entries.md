# Time Entries API

## Обзор

Учёт затраченного времени на задачи.

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | `/time_entries` | Создать запись |
| GET | `/time_entries` | Список записей |
| GET | `/time_entries/{id}` | Запись по ID |
| PATCH | `/time_entries/{id}` | Обновить запись |
| DELETE | `/time_entries/{id}` | Удалить запись |

## Модель данных

```json
{
  "task_id": 5,
  "start_time": "2024-01-15T09:00:00",
  "end_time": "2024-01-15T11:30:00",
  "duration": 150
}
```

## Примеры

### Создание записи

```
POST /time_entries
Content-Type: application/json

{
  "task_id": 5,
  "start_time": "2024-01-15T09:00:00",
  "end_time": "2024-01-15T11:30:00",
  "duration": 150
}
```

**Ответ 201:**
```json
{
  "status": 201,
  "data": {
    "id": 1,
    "task_id": 5,
    "start_time": "2024-01-15T09:00:00",
    "end_time": "2024-01-15T11:30:00",
    "duration": 150
  }
}
```

### Список записей

```
GET /time_entries
```

**Ответ:**
```json
[
  {
    "id": 1,
    "task_id": 5,
    "start_time": "2024-01-15T09:00:00",
    "end_time": "2024-01-15T11:30:00",
    "duration": 150
  }
]
```

### Удаление

```
DELETE /time_entries/1
```

**Ответ:**
```json
{"ok": true}
