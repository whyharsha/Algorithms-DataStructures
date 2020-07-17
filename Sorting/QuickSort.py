def quick_sort(list_of_comparables):
    """
    Sorts the list of numbers using quick sort.
    Returns the sorted list.
    """

    if list_of_comparables is None:
        raise ValueError

    if len(list_of_comparables) == 0:
        return list_of_comparables
    
    __quick_sort(list_of_comparables, 0, len(list_of_comparables) - 1)

    return list_of_comparables

def __quick_sort(list_of_comparables, left: int, right: int):
    if left > right:
        return

    pivot_index = __partition(list_of_comparables, left, right)
    __quick_sort(list_of_comparables, left, pivot_index - 1)
    __quick_sort(list_of_comparables, pivot_index + 1, right)
    
def __partition(list_of_comparables, left: int, right: int):
    
    pivot = list_of_comparables[left]

    while True:

        while list_of_comparables[left] <= pivot and left <= right:
            left += 1
        
        while list_of_comparables[right] >= pivot and left <= right:
            right -= 1
        
        if left <= right:
            list_of_comparables[left], list_of_comparables[right] = list_of_comparables[right], list_of_comparables[left]
        else:
            break
    
    list_of_comparables[pivot], list_of_comparables[right] = list_of_comparables[right], list_of_comparables[pivot]

    return right
        
    


