import random
from settings import Settings



class Data(Settings):
    @classmethod
    def random(cls):
        data = [random.randint(cls.MIN_VAL, cls.MAX_VAL) for _ in range(cls.SIZE)]
        return data

    @classmethod
    def reversed(cls):
        data = list(
                    range(cls.SIZE if cls.SIZE > cls.MAX_VAL else cls.MAX_VAL,
                    cls.MIN_VAL - 1, -1))[:cls.SIZE]
        return data

    @classmethod
    def few_unique(cls):
        data = [random.randint(cls.MIN_VAL, cls.MAX_VAL) for _ in
                range(cls.SIZE - (2 * (cls.SIZE // 3)))] + [
                   cls.MAX_VAL // 2] * (cls.SIZE // 3) + [cls.MAX_VAL] * (
                       cls.SIZE // 3)
        random.shuffle(data)
        return data
