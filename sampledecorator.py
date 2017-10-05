import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        x = func(*args, **kwargs)
        end = time.time()
        print('function ' + func.__name__ + ' took ' + str(
            end - start) + ' seconds')
        return x
    return wrapper


@timer
def test_function(x, y, z=2):
    return x + y + z


test_function(2, 3)
