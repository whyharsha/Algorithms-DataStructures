#the straightforward version - O(n)
#finds all peaks of an unsorted array
def peakfinder_one_dim_greedy(list_of_comparables):
    if(list_of_comparables is None):
        raise ValueError

    size_of_list = len(list_of_comparables)
    peaks = {}

    if(size_of_list > 1):
        #go left to right and check left and right
        for index in range(size_of_list):
            if(index == 0):
                if(list_of_comparables[index] > list_of_comparables[index + 1]):
                    peaks[index] = list_of_comparables[index]
                    
            elif(index == (size_of_list - 1)):
                if(list_of_comparables[index] > list_of_comparables[index - 1]):
                    peaks[index] = list_of_comparables[index]

            else:
                if(size_of_list > 2 and (list_of_comparables[index] > list_of_comparables[index + 1]) and (list_of_comparables[index] > list_of_comparables[index - 1])):
                    peaks[index] = list_of_comparables[index]

    else:
        if(size_of_list > 0):
            peaks[0] = list_of_comparables[0]

    return peaks

#a recursive binary search to find a peak (not all peaks)
#assume array having atleast one element
#O(log2n)
def peakfinder_one_dim_binary(list_of_comparables):
    if(list_of_comparables is None):
        raise ValueError

    size_of_list = len(list_of_comparables)

    if(size_of_list == 1):
        return (0, list_of_comparables[0])
    
    if(size_of_list == 2):
        if (list_of_comparables[0] > list_of_comparables[1]):
            return (0, list_of_comparables[0])

        else:
            return (1, list_of_comparables[1])
    
    if(size_of_list > 2):
        middle = size_of_list // 2

        matchvalue = 0

        if(list_of_comparables[middle] < list_of_comparables[middle - 1]):
            matchvalue += 1

        if(list_of_comparables[middle] < list_of_comparables[middle + 1]):
            matchvalue += 2
        
        #only left value is bigger than our current value
        if (matchvalue == 1):
            peakfinder_one_dim_binary(list_of_comparables[0:middle])

        #only right value is bigger than our current value
        elif (matchvalue == 2):
            peakfinder_one_dim_binary(list_of_comparables[middle:size_of_list])

        #left and right are bigger than our current value
        elif (matchvalue == 3):
            #right is bigger than the left value
            if(list_of_comparables[middle - 1] < list_of_comparables[middle + 1]):
                peakfinder_one_dim_binary(list_of_comparables[middle:size_of_list])
            else:
                peakfinder_one_dim_binary(list_of_comparables[0:middle])

        else:
            return (middle, list_of_comparables[middle])
    
    #should not get called unless there is a bug
    return (None, None) 

def get_row_col_count(input_2d_array):
    if(input_2d_array is None):
        raise ValueError

    row_count = len(input_2d_array)
    col_count = 0

    for row in input_2d_array:
        count = len(row) #reduce number of calculations of row length by using a count variable
        if(count > col_count):
            col_count = count
    
    return (row_count, col_count)

#a greedy ascent algo to find a peak for a 2d array
#O(nm) where n and m are size of the rows and columns
#assume a 2d array as input with equal size columns, not validating
def peakfinder_two_dim_greedy(input_array):
    if(input_array is None):
        raise ValueError

    (row_count, col_count) = get_row_col_count(input_array)
    
    if(row_count > 1 and col_count > 1):
        for x in range(row_count):
            for y in range(col_count):
                if(x == 0):
                    if(y == 0):
                        if(input_array[x][y] > input_array[x+1][y] and input_array[x][y] > input_array[x][y+1]):
                            return input_array[x][y]

                    elif(y == col_count - 1):
                        if(input_array[x][y] > input_array[x+1][y] and input_array[x][y] > input_array[x][y-1]):
                            return input_array[x][y]

                    else:
                        if(input_array[x][y] > input_array[x+1][y] and input_array[x][y] > input_array[x][y-1] and input_array[x][y] > input_array[x][y+1]):
                            return input_array[x][y]

                elif(x == row_count - 1):
                    if(y == 0):
                        if(input_array[x][y] > input_array[x-1][y] and input_array[x][y] > input_array[x][y+1]):
                            return input_array[x][y]

                    elif(y == col_count - 1):
                        if(input_array[x][y] > input_array[x-1][y] and input_array[x][y] > input_array[x][y-1]):
                            return input_array[x][y]

                    else:
                        if(input_array[x][y] > input_array[x-1][y] and input_array[x][y] > input_array[x][y-1] and input_array[x][y] > input_array[x][y+1]):
                            return input_array[x][y]

                else:
                    if(y == 0):
                        if(input_array[x][y] > input_array[x+1][y] and input_array[x][y] > input_array[x-1][y] and input_array[x][y] > input_array[x][y+1]):
                            return input_array[x][y]

                    elif(y == col_count - 1):
                        if(input_array[x][y] > input_array[x+1][y] and input_array[x][y] > input_array[x-1][y] and input_array[x][y] > input_array[x][y-1]):
                            return input_array[x][y]

                    else:
                        if(input_array[x][y] > input_array[x+1][y] and input_array[x][y] > input_array[x-1][y] and input_array[x][y] > input_array[x][y-1] and input_array[x][y] > input_array[x][y+1]):
                            return input_array[x][y]

    else:
        if(row_count == 1 and col_count > 1):
            (index, value) = peakfinder_one_dim_binary(input_array[0])

            if(index is not None):
                return input_array[0][index]

            else:
                return None

        elif(row_count > 1 and col_count == 1):
            new_array = []
            
            for row in input_array:
                new_array.append(row[0])
            
            (index, value) = peakfinder_one_dim_binary(new_array)

            if(index is not None):
                return input_array[0][index]

            else:
                return None

        elif(row_count == 1 and col_count == 1):
            return input_array[0][0]

        else:
            return None

#a version of recursive binary search on 2D to return a peak
#O(nlog2m)
def peakfinder_two_dim_binary(input_array):
    if(input_array is None):
        raise ValueError
    
    (row_count, col_count) = get_row_col_count(input_array)

    if (row_count > 2):
        mid_r = row_count // 2

        #this should never receive a (None, None), if it does, there is a high-pri bug to be fixed
        (col, value) = peakfinder_one_dim_binary(input_array[mid_r])

        matchvalue = 0

        if (input_array[mid_r][col] < input_array[mid_r - 1][col]):
            matchvalue += 1
                    
        if (input_array[mid_r][col] < input_array[mid_r + 1][col]):
            matchvalue += 2
                    
        #only the top row is bigger than our current value
        if (matchvalue == 1):
            peakfinder_two_dim_binary(input_array[0:mid_r])

        #only the bottom row is bigger than our current value
        elif (matchvalue == 2):
            peakfinder_two_dim_binary(input_array[mid_r:row_count])

        #both top and bottom rows have bigger values
        elif (matchvalue == 3):
            #bottom row is bigger than the top row
            if (input_array[mid_r - 1][col] < input_array[mid_r + 1][col]):
                peakfinder_two_dim_binary(input_array[mid_r:row_count])

            else:
                peakfinder_two_dim_binary(input_array[0:mid_r])

        else:
            #a tuple that provides, the row, column and value
            return (mid_r, col, input_array[mid_r][col])

    elif(row_count == 1):
        #returns a tuple with row, col and value
        return (0, ) + peakfinder_one_dim_binary(input_array[0])

    elif(row_count == 2):
            (col1, value1) = peakfinder_one_dim_binary(input_array[0])
            (col2, value2) = peakfinder_one_dim_binary(input_array[1])

            if(value1 > value2):
                return (0, col1, value1)

            else:
                return (1, col2, value2)

    else:
        return (None, None, None)





