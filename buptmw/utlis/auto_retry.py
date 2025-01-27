from time import sleep


def auto_retry_network_connections(func):
    def wrapper(*args, **kwargs):
        MAX_TIMES = 5
        for time in range(1, MAX_TIMES + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"{time}th Network connection failed with an exception: {e}")
                if time < MAX_TIMES:
                    print("Retrying...")
                    sleep(1)
                else:
                    print("Reach max retries. Stop.")
                    raise e
    return wrapper
