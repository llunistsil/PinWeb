# Подключение к базе данных

## Настройка

Приложение использует PostgreSQL через SQLModel (ORM на основе SQLAlchemy).

## Переменные окружения

| Переменная | Описание |
|------------|----------|
| `DB_ADMIN` | Строка подключения к БД |

## Пример .env

```
DB_ADMIN=postgresql://user:password@localhost:5432/dbname
```

## Инициализация

```python
from src.db.connection import init_db, get_session

# Создание таблиц
init_db()

# Получение сессии
for session in get_session():
    # работа с БД
    pass
```

## Сессия

Генератор `get_session()` предоставляет сессию для каждого запроса и автоматически закрывает её после использования.
