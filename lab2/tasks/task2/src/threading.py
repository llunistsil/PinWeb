import threading
import time

from lab2.tasks.task2.src.connection import init_db
from urls import urls
from lab2.tasks.task2.src.parse_and_save import parse_and_save


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
