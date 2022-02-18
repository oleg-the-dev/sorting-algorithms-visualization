import random


def bogo_sort(data, *args):
    sorted_data = sorted(data)
    while data != sorted_data:
        random.shuffle(data)
        yield data, -1, -1, -1, -1
