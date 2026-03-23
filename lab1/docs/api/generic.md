# Generic API

## Обзор

Базовые CRUD операции для работы с базой данных.

## Функции

| Функция | Описание |
|---------|----------|
| `create_object` | Создание записи в БД |
| `read_object_list` | Получение всех записей |
| `read_object` | Получение записи по ID |
| `update_object` | Обновление записи |
| `delete_object` | Удаление записи |

## Сигнатуры

```python
create_object(session: Session, input_model: InputModel, output_model: Type[OutputModel]) -> Response[OutputModel]

read_object_list(session: Session, output_model: Type[OutputModel]) -> List[OutputModel]

read_object(session: Session, id: int, output_model: Type[OutputModel]) -> OutputModel

update_object(session: Session, id: int, input_model: InputModel, output_model: Type[OutputModel]) -> InputModel

delete_object(session: Session, id: int, output_model: Type[OutputModel]) -> dict
```

## Пример использования

```python
# Создание
result = create_object(session, user_data, User)

# Список всех
users = read_object_list(session, User)

# По ID
user = read_object(session, user_id, User)

# Обновление
updated = update_object(session, user_id, user_data, User)

# Удаление
delete_object(session, user_id, User)
