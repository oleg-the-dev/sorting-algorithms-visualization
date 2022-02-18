def insertion_sort(data, *args):
    sorted_data = []
    for i in range(0, len(data)):
        j = i - 1
        key = data[i]
        sorted_data.append(i)
        while j >= 0 and data[j] > key:
            yield data, j, -1, i, -1
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    sorted_data.clear()
