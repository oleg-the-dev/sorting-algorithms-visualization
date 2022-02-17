def bubble_sort(data, *args):
    for i, _ in enumerate(data):
        for j, _ in enumerate(data[:len(data) - i - 1]):
            yield data, j-1, -1, j, len(data) - i
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

