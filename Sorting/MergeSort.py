def merge_sort(list_of_items):
    """
    Performs a merge sort on the list of items
    Returns: a sorted list
    """
    if not list_of_items is None and len(list_of_items) > 0:
        
        list_len = len(list_of_items)

        if list_len == 1:
            return list_of_items

        sorted_list = []

        #sort the left half
        left_list = merge_sort(list_of_items[0:(list_len // 2)])
        #sort the right half
        right_list = merge_sort(list_of_items[(list_len // 2): list_len])
        #merge the halves
        return __merge(left_list, right_list)
    
    return list_of_items

def __merge(left_list, right_list):
    """
    Takes sorted lists and merges them into a sorted list
    """

    sorted_list = []

    left, right = 0, 0 

    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            sorted_list.append(left_list[left])
            left += 1
        else:
            sorted_list.append(right_list[right])
            right += 1
    
    if left == len(left_list):
        sorted_list.extend(right_list[right:])
    else:
        sorted_list.extend(left_list[left:])
    
    return sorted_list

