# Notifications API

## Обзор

Управление уведомлениями о задачах.

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| POST | `/notifications` | Создать уведомление |
| GET | `/notifications` | Список уведомлений |
| GET | `/notifications/{id}` | Уведомление по ID |
| PATCH | `/notifications/{id}` | Обновить |
| DELETE | `/notifications/{id}` | Удалить |

## Модель данных

```json
{
  "task_id": 1,
  "message": "Напоминание о задаче",
  "sent_at": "2024-01-15T10:30:00"
}
```

## Примеры

### Создание

```
POST /notifications
Content-Type: application/json

{
  "task_id": 5,
  "message": "Дедлайн завтра!"
}
```

### Получение списка

```
GET /notifications
```

**Ответ:**
```json
[
  {
    "id": 1,
    "task_id": 5,
    "message": "Дедлайн завтра!",
    "sent_at": "2024-01-15T10:30:00"
  }
]
