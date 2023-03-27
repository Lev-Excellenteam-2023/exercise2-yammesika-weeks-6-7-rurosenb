import time


def timer(f, *args, **kwargs):
    """
    Measures the execution time of a function with the given parameters.
    """
    start_time = time.time()
    f(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))