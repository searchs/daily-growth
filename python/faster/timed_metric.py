from functools import wraps
from time import monotonic


def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = monotonic()
        try:
            return fn(*args, **kwargs)
        finally:
            duration = monotonic() - start
            # Save result to DB
            print("{} took {:.3f}sec".format(fn.__name__, duration))

    return wrapper


if __name__ == "__main__":
    # Example usage:
    from time import sleep

    @timed
    def add(a, b):
        sleep(a / 10)
        return a + b
