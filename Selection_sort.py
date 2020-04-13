def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        number = find_the_smallest(array)
        new_array.append(array[number])
        array.pop(number)
    return new_array
def find_the_smallest(array):
    index = 0
    lowest = array[0]
    for i in array:
        if lowest > i:
            lowest = i
            index  = array.index(i)
    return index

print(selection_sort([5,3,6,8,2,1,4,6,7]), selection_sort([1, 2, 3, 4, 5, 6, 6, 7, 8]),sep="\n")