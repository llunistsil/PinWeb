# Схема базы данных

## Таблицы

### users
Хранит учётные записи пользователей.

| Поле | Тип | Описание |
|------|-----|----------|
| id | int | Первичный ключ |
| first_name | string | Имя |
| last_name | string | Фамилия |
| username | string | Логин |
| email | string | Email |
| password_hash | string | Хэш пароля |

### priorities
Справочник приоритетов задач.

| Поле | Тип | Описание |
|------|-----|----------|
| id | int | Первичный ключ |
| name | string | Название |

### tasks
Задачи пользователей.

| Поле | Тип | Описание |
|------|-----|----------|
| id | int | Первичный ключ |
| description | string | Описание |
| deadline | datetime | Срок выполнения |
| priority_id | int | Внешний ключ на priorities |
| user_id | int | Внешний ключ на users |

### schedules
Расписание пользователей.

| Поле | Тип | Описание |
|------|-----|----------|
| id | int | Первичный ключ |
| user_id | int | Внешний ключ на users |
| date | datetime | Дата |

### schedule_tasks
Связь расписания и задач (многие-ко-многим).

| Поле | Тип | Описание |
|------|-----|----------|
| schedule_id | int | Внешний ключ на schedules |
| task_id | int | Внешний ключ на tasks |
| added_at | datetime | Дата добавления |

### time_entries
Учёт затраченного времени.

| Поле | Тип | Описание |
|------|-----|----------|
| id | int | Первичный ключ |
| task_id | int | Внешний ключ на tasks |
| start_time | datetime | Начало |
| end_time | datetime | Окончание |
| duration | int | Длительность (сек) |

### notifications
Уведомления о задачах.

| Поле | Тип | Описание |
|------|-----|----------|
| id | int | Первичный ключ |
| task_id | int | Внешний ключ на tasks |
| message | string | Текст |
| sent_at | datetime | Время отправки |
