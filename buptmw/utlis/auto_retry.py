from requests.exceptions import RequestException
from time import sleep


def auto_retry_network_connections(func):
    def wrapper(*args, **kwargs):
        MAX_TIMES = 5
        for time in range(MAX_TIMES):
            try:
                return func(*args, **kwargs)
            except RequestException as e:
                print(f"{time + 1}th Network connection failed with an exception: {e}")
                if time < MAX_TIMES - 1:
                    print("Retrying...")
                    sleep(1)
                else:
                    print("Reach max retries. Stop.")
                    raise e
    return wrapper
