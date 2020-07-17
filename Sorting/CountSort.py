#Sort in linear time O(n+k)
#assume values sorted are integers
#each of which fit in a machine-word (32/64 bit)
#assume each value in the integer array was of the form (int, object) i.e. a key-value pair
#should be possible to extend the code to accommodate that
#the last for-loop would be a touch more complex to keep it in stable sorting order
#the implementation below only outlines the basic idea

def counting_sort(integer_array, largest_possible_value: int):
    """
    Sorts given array using counting sort.
    Returns a sorted array.
    """
    counter = [0] * (largest_possible_value + 1) #size k where k is 1 + largest_possible_value
    sorted_list = [0] * len(integer_array) #size n
    
    for value in integer_array:
        counter[value] += 1

    counter = aggregate_sum(counter)
    
    for value in integer_array:
        sorted_list[counter[value] - 1] = value
        counter[value] -= 1
    
    return sorted_list

def aggregate_sum(array):
    for index in (1, len(array)):
        array[index] = array[index] + array[index - 1]
    
    return array