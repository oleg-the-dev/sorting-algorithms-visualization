def selection_sort(data, *args):
    for i in range(len(data) - 1):
        curr_min = i
        for j in range(i, len(data)):
            if data[j] < data[curr_min]:
                curr_min = j
            yield data, j, -1, i, curr_min
        data[i], data[curr_min] = data[curr_min], data[i]
