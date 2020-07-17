class BinaryHeap(object):
    """
    Implements a priority queue with a binary tree structure.
    """
    
    def __init__(self, heaptype = "min"):
        """
        Initializes a binary tree heap with a default type of min.
        Pass heaptype = "max", if you need a max heap
        """
        self.heap = [] #an empty array to store elements

        if not (heaptype == "min" or heaptype == "max"):
            raise ValueError

        self.heaptype = heaptype
    
    def is_empty(self):
        """
        Returns true if the heap is empty, false if not.
        """
        if len(self.heap) == 0:
            return True
        
        return False
    
    def min(self):
        """
        Returns the minimum value of the heap in a min heap.
        IndexError if the heap size is 0.
        """
        if len(self.heap) == 0:
            raise IndexError

        return self.heap[0]
    
    def max(self):
        """
        Returns the maximum value of the heap in a max heap.
        IndexError if the heap size is 0.
        """
        if len(self.heap) == 0:
            raise IndexError

        return self.heap[0]

    def extract_min(self):
        """
        Returns the minimum value of the heap in a min heap and removes it.
        IndexError if the heap size is 0.
        """
        if len(self.heap) == 0:
            raise IndexError
        
        value = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap) - 1)
        self.__min_heapify_down(0)

        return value
    
    def extract_max(self):
        """
        Returns the maximum value of the heap in a max heap and removes it.
        IndexError if the heap size is 0.
        """
        if len(self.heap) == 0:
            raise IndexError

        value = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap) - 1)
        self.__max_heapify_down(0)
    
    def insert(self, value):
        """
        Inserts a value into the heap.
        """
        if len(self.heap) == 0:
            self.heap.append(value)
        else:
            self.heap.append(value)

            if self.heaptype == "min":
                self.__min_heapify_up(len(self.heap - 1))
            
            if self.heaptype == "max":
                self.__max_heapify_up(len(self.heap - 1))
    
    def __min_heapify_up(self, index: int):
        if self.__has_parent(index) and self.__get_parent(index) > self.heap[index]:
                self.__swap(self.__get_parent_index(index), index)
                self.__min_heapify_up(self.__get_parent_index(index))
    
    def __max_heapify_up(self, index: int):
        if self.__has_parent(index) and self.__get_parent(index) < self.heap[index]:
                self.__swap(self.__get_parent_index(index), index)
                self.__max_heapify_up(self.__get_parent_index(index))

    def __min_heapify_down(self, index: int):
        smallest = index

        if self.__has_left_child(index) and self.__get_left_child(index) < self.heap[index]:
            smallest = self.__get_left_child_index(self, index)
            
        if self.__has_right_child(index) and self.__get_right_child(index) < self.heap[smallest]:
            smallest = self.__get_right_child_index(self, index)
        
        if not smallest == index:
            self.__swap(index, smallest)
            self.__min_heapify_down(smallest)

    def __max_heapify_down(self, index: int):
        largest = index

        if self.__has_left_child(index) and self.__get_left_child(index) > self.heap[index]:
            largest = self.__get_left_child_index(self, index)
        
        if self.__has_right_child(index) and self.__get_right_child(index) < self.heap[largest]:
            largest = self.__get_right_child_index(self, index)
        
        if not largest == index:
            self.__swap(index, largest)
            self.__max_heapify_down(largest)

    def __get_left_child(self, index: int):
        return self.heap[self.__get_left_child_index(index)]
    
    def __get_right_child(self, index: int):
        return self.heap[self.__get_right_child_index(index)]

    def __get_parent(self, index: int):
        return self.heap[self.__get_parent_index(index)]
    
    def __get_left_child_index(self, index: int): 
        return ((2 * index) + 1)

    def __get_right_child_index(self, index: int):
        return ((2 * index) + 2)

    def __get_parent_index(self, index: int):
        return ((index - 1) // 2 )
    
    def __has_left_child(self, index: int):
        return (self.__get_left_child_index(index) < len(self.heap))

    def __has_right_child(self, index: int):
        return (self.__get_right_child_index(index) < len(self.heap))
    
    def __has_parent(self, index: int):
        return (self.__get_parent_index(index) >= 0)
    
    def __swap(self, one: int, other: int):
        self.heap[one], self.heap[other] = self.heap[other], self.heap[one]
