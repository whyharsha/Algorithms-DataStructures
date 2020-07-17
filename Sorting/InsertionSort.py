#O(n-squared)
def insertion_sort_basic(list_of_items):
    """
    Sorts the given list of items using insertion sort
    Returns: sorted list
    """
    if list_of_items is None:
        raise ValueError

    list_len = len(list_of_items)

    for key in range(list_len):
        index = key - 1
        while index >= 0:
            if(list_of_items[key] < list_of_items[index]):
                list_of_items[key], list_of_items[index] = list_of_items[index], list_of_items[key]
                index -= 1
            else:
                break
    
    return list_of_items

def insertion_sort_binary(list_of_items):
    """
    Sorts the given list of items using insertion sort
    Returns: sorted list
    """
    if list_of_items is None:
        raise ValueError

    list_len = len(list_of_items)

    return list_of_items
