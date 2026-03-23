# Схема базы данных

## ER-диаграмма

```
users (1) ──────< (N) tasks
  │                │
  │                │ (N)
  │                └──────> (1) priorities
  │
  │ (1)
  │
  └──────< (N) schedules
                 │
                 │ (N)
                 └──────< (M) schedule_tasks >──────> (M) tasks
                                                        
tasks (1) ──────< (N) time_entries
  │
  │ (1)
  └──────< (N) notifications
```

## Описание таблиц

### users
| Поле | Тип | Ограничения |
|------|-----|-------------|
| id | INTEGER | PRIMARY KEY |
| first_name | VARCHAR | |
| last_name | VARCHAR | |
| username | VARCHAR | UNIQUE, NOT NULL |
| email | VARCHAR | UNIQUE, NOT NULL |
| password_hash | VARCHAR | |

### priorities
| Поле | Тип | Ограничения |
|------|-----|-------------|
| id | INTEGER | PRIMARY KEY |
| name | VARCHAR | NOT NULL |

### tasks
| Поле | Тип | Ограничения |
|------|-----|-------------|
| id | INTEGER | PRIMARY KEY |
| description | TEXT | NOT NULL |
| deadline | TIMESTAMP | NOT NULL |
| priority_id | INTEGER | FOREIGN KEY → priorities.id |
| user_id | INTEGER | FOREIGN KEY → users.id |

### schedules
| Поле | Тип | Ограничения |
|------|-----|-------------|
| id | INTEGER | PRIMARY KEY |
| user_id | INTEGER | FOREIGN KEY → users.id |
| date | TIMESTAMP | NOT NULL |

### schedule_tasks
| Поле | Тип | Ограничения |
|------|-----|-------------|
| schedule_id | INTEGER | PRIMARY KEY, FK → schedules.id |
| task_id | INTEGER | PRIMARY KEY, FK → tasks.id |
| added_at | TIMESTAMP | DEFAULT NOW() |

### time_entries
| Поле | Тип | Ограничения |
|------|-----|-------------|
| id | INTEGER | PRIMARY KEY |
| task_id | INTEGER | FOREIGN KEY → tasks.id |
| start_time | TIMESTAMP | NOT NULL |
| end_time | TIMESTAMP | NOT NULL |
| duration | INTEGER | NOT NULL |

### notifications
| Поле | Тип | Ограничения |
|------|-----|-------------|
| id | INTEGER | PRIMARY KEY |
| task_id | INTEGER | FOREIGN KEY → tasks.id |
| message | TEXT | NOT NULL |
| sent_at | TIMESTAMP | NOT NULL |
