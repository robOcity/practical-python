# timethis.py
#
# Define decorator to time function calls, maybe a few more too.


def timethis(func):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__module__}, {func.__name__}, {end-start}s")

    return wrapper
