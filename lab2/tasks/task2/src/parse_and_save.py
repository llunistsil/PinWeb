from bs4 import BeautifulSoup
import requests

from lab2.tasks.task2.src.connection import SessionLocal
from lab2.tasks.task2.src.models import WebPage


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
