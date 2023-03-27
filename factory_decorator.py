import functools


def check_type(expected_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            try:
                if not isinstance(arg, expected_type):
                    raise Exception(f"Expected {expected_type}, but got {type(arg)}")
                return func(arg)
            except Exception as e:
                return e

        return wrapper

    return decorator


if __name__ == '__main__':
    @check_type(int)
    def times2(num):
        return num * 2


    print("using 5: ", times2(5))
    print("using str(5): ", times2("5"))
