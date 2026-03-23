from bs4 import BeautifulSoup

from lab2.tasks.task2.src.connection_async import SessionLocal_async
from lab2.tasks.task2.src.models import WebPage


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
