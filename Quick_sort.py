def quick_sort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        lesser = quick_sort([x for x in array[1:] if x < pivot])
        greater = quick_sort([x for x in array[1:] if x >= pivot])
        return lesser + [pivot] + greater

print(quick_sort([5,3,3,6,7,56,4,5,6,7,8]))
