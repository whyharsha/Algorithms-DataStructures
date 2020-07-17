import math

def radix_sort(integer_array):
    """
    Uses radix sort to sort the array.
    Assumes the values in the array are integers within range of size of array
    Returns a sorted integer array
    """
    maximum = max(integer_array)
    radix = len(integer_array)

    number_of_digits = get_number_of_digits(maximum, radix)

    for pos in range(number_of_digits):
        integer_array = counting_sort(integer_array, maximum, pos)
    
    return integer_array

def counting_sort(integer_array, largest_possible_value: int, pos: int):
    radix = len(integer_array)
    counter = [0] * radix

    for value in integer_array:
        counter[get_digit(value, radix, pos)] += 1
        
    counter = aggregate_sum(counter)

    sorted_list = [0] * radix

    for value in integer_array:
        digit = get_digit(value, radix, pos)
        sorted_list[counter[digit] - 1] = value
        counter[value] -= 1

def aggregate_sum(array):
    for index in (1, len(array)):
        array[index] = array[index] + array[index - 1]
    
    return array        

def get_number_of_digits(value: int, radix: int) -> int:
    """
    Returns the number of digits in the value (decimal) in base radix.
    """
    return (math.floor(math.log(value)/math.log(radix)) + 1)

def get_digit(value: int, radix: int, pos: int):
    """
    Returns the digit of value (decimal) in base radix at position pos.
    """
    return (value // radix ** pos) % radix