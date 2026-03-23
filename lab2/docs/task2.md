# Задача 2. Параллельный парсинг сайтов с сохранением в БД

**Задание**: Создать программу для параллельного сбора данных с веб-страниц используя threading, multiprocessing и asyncio. Данные сохраняются в базу данных PostgreSQL.

## Модель данных

```python
from sqlmodel import Field, SQLModel
from typing import Optional


class WebPage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str
    title: str
```

## Функция парсинга для async

```python
from bs4 import BeautifulSoup

from connection_async import SessionLocal_async
from models import WebPage


async def parse_and_save_async(url, session):
    try:
        async with session.get(url) as response:
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            page_title = soup.title.string if soup.title else 'No title found'

            async with SessionLocal_async() as db_session:
                page = WebPage(url=url, title=page_title)
                db_session.add(page)
                await db_session.commit()
        print(f"Saved: {url} - {page_title}")
    except Exception as e:
        print(f"Failed to parse {url}: {e}")
```

## Asyncio реализация

```python
import aiohttp
import asyncio
import time

from urls import urls
from parse_and_save_async import parse_and_save_async
from connection_async import init_db_async


async def main():
    await init_db_async()
    
    async with aiohttp.ClientSession() as session:
        tasks = [parse_and_save_async(url, session) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Async execution time: {end_time - start_time} seconds")
```

## Функция парсинга (sync)

```python
from bs4 import BeautifulSoup
import requests

from connection import SessionLocal
from models import WebPage


def parse_and_save(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_title = soup.title.string if soup.title else 'No title found'

        with SessionLocal() as session:
            page = WebPage(url=url, title=page_title)
            session.add(page)
            session.commit()
        print(f"Saved: {url} - {page_title}")
    except Exception as e:
        print(f"Failed to parse {url}: {e}")
```

## Multiprocessing реализация

```python
import multiprocessing
import time

from connection import init_db
from urls import urls
from parse_and_save import parse_and_save


def main():
    init_db()
    
    processes = []
    start_time = time.time()

    for url in urls:
        process = multiprocessing.Process(target=parse_and_save, args=(url,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
```

## Threading реализация

```python
import threading
import time

from connection import init_db
from urls import urls
from parse_and_save import parse_and_save


def main():
    init_db()
    
    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=parse_and_save, args=(url,))
        threads.append(thread)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Threading execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
```

## Результаты

Парсинг одного ресурса:

![Результат](img/one_out.png)

Парсинг пяти ресурсов:

![Результат](img/t2out.png)

## Выводы

Для I/O операций (парсинг сайтов):
- **threading** и **asyncio** показывают наилучшие результаты
- **multiprocessing** менее эффективен из-за накладных расходов на создание процессов
- Для большого количества запросов threading может быть стабильнее чем aiohttp
