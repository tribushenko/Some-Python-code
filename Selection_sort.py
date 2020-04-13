def selection_sort(array):
    sorted_array = []
    for i in range(len(array)):
        index = find_the_smallest(array)
        sorted_array.append(array[index])
        array.pop(index)
    return sorted_array


def find_the_smallest(array):
    index = 0
    smallest = array[0]
    for i in array:
        if smallest > i:
            smallest = i
            index = array.index(smallest)
    return index


print(selection_sort([3, 5, 6, 8, 5, 4, 3, 1, 2, 3, 4]))
