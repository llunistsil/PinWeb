# Задача 2: Интеграция парсера в FastAPI приложение

## Эндпоинт для вызова парсера

Добавлен маршрут в FastAPI для приёма URL от клиента и передачи запроса парсеру в отдельном контейнере.

```python
from fastapi import APIRouter, HTTPException, status
import requests


router = APIRouter(prefix="/parser", tags=["parser"])


@router.post("/")
def parse_site(url: str):
    try:
        response = requests.post("http://parser:8000/parse",
                                 json={"url": url})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```

## Особенности

При использовании docker-compose сервисы автоматически объединяются в общую сеть, что позволяет обращаться к ним по имени сервиса (в данном случае `parser`). Явное указание сети в docker-compose необязательно, но возможно для лучшей организации.
