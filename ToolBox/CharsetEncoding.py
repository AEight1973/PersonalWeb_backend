import random
import string


def random_str(_num):
    _set = string.digits + string.ascii_letters
    _str = ''
    for _ in range(_num):
        _str += random.choice(_set)
    return _str


if __name__ == '__main__':
    print(random_str(5))
