from threading import Thread
import time
import requests
from loguru import logger

from queue import Queue



SYMBOLS = ('USD', 'EUR', 'PLN', 'GBP', 'CHF', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'GBP', 'CHF', 'NOK', 'CZK')

# BASE_URL = "http://api.exchangeratesapi.io/v1/latest?access_key=YOUR_ACCESS_KEY"
BASE_URL = "https://api.vatcomply.com/rates"

def fetch_data(base):
    response = requests.get(f"{BASE_URL}?base={base}")
    response.raise_for_status()
    rates = response.json()["rates"]

    # same currency
    rates[base] = 1.0
    rates_line = ", ".join(
        [f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    logger.info(f"1 {base} = {rates_line}\n")
    # return response.json()


def worker(work_queue):
    while not work_queue.empty():
        try:
            item = work_queue.get_nowait()
        except Empty:
            break
        else:
            fetch_data(item)
            work_queue.task_done()


def main():
    threads = [Thread(target=fetch_data, args=(base,)) for base in BASES]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def main_thread():
    threads = []
    for base in BASES:
        thread = Thread(target=fetch_data, args=[base])
        thread.start()
        threads.append(thread)
    while threads:
        threads.pop().join()

THREAD_POOL_SIZE = 4

def main_thread_pool():
    work_queue = Queue()
    for base in BASES:
        work_queue.put(base)
    threads = [Thread(target=worker, args=(work_queue,)) for _ in range(THREAD_POOL_SIZE)]
    for thread in threads:
        thread.start()
    work_queue.join()
    while threads:
        threads.pop().join()

if __name__ == "__main__":
    started = time.time()
    main_thread_pool()
    elapsed = time.time() - started
    logger.info(f"Time taken: {elapsed:.2f}s")
