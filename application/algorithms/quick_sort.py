from random import randint


def quick_sort(array, left, right):
    if left >= right:
        return
    index = left
    random_index = randint(left, right)
    array[right], array[random_index] = array[random_index], array[right]

    for j in range(left, right):
        yield array, j, right, index, -1
        if array[j] < array[right]:
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    yield from quick_sort(array, index + 1, right)
    yield from quick_sort(array, left, index - 1)
