import random
from settings import Settings


class Data(Settings):
    @classmethod
    def random(cls):
        data = [random.randint(cls.MIN_VAL, cls.MAX_VAL) for _ in
                range(cls.SIZE)]
        return data

    @classmethod
    def reversed(cls):
        data = [random.randint(cls.MIN_VAL, cls.MAX_VAL) for _ in
                range(cls.SIZE)]
        data.sort(reverse=True)
        return data

    @classmethod
    def few_unique(cls):
        data = [random.randint(cls.MIN_VAL, cls.MAX_VAL) for _ in
                range(cls.SIZE - (2 * (cls.SIZE // 3)))] + [
                   cls.MAX_VAL // 2] * (cls.SIZE // 3) + [cls.MAX_VAL] * (
                       cls.SIZE // 3)
        random.shuffle(data)
        return data
