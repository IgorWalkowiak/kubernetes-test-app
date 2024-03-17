import random
import time


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    for x in range(5):
        time.sleep(random.randint(1, 10))
        print_hi('PyCharm ' + str(x))
exit(0)
