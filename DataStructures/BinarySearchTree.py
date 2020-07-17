from DataStructures.TreeNode import TreeNode

class BinarySearchTree(object):
    """
    Implements a binary search tree.
    Advantage is a host of operations at O(log(n)) or less
    """

    def __init__(self, unique = True):
        """
        Initialize the binary search tree with an empty root node
        Unique, when true, means the tree will not insert any duplicate values.
        """

        #Keeping both root and size private so cannot be modified externally
        self.__root = TreeNode(0, None, None)
        self.__size = 0
        self.__unique = unique
    
    def __init__(self, root: TreeNode, unique = True):
        """
        Initialize the binary search tree with a given Node
        """

        self.__root = root
        self.__unique = unique

        if self.__root is None:
            self.__size = 0
        else:
            self.__size = 1
    
    def is_empty(self):
        """
        Returns true if the tree is empty.
        """
        return self.__size == 0

    def size(self):
        """
        Returns the size of the binary search tree.
        """
        return self.__size
    
    def is_unique(self):
        """
        Returns true if the search tree will hold only unique elements.
        """
        return self.__unique
    
    def height(self):
        """
        Computes and returns the height of the tree.
        """
        if self.__root is None or self.size() == 0:
            return 0
        else:
            return self.__height(0, self.__root)
    
    def __height(self, current_height: int, node: TreeNode):
        height = current_height + 1
        l_height, r_height = height, height

        if node.has_l_child():
            l_height = self.__height(node.left, l_height)
        
        if node.has_r_child():
            r_height = self.__height(node.right, r_height)
        
        if height < max(l_height, r_height):
            height = max(l_height, r_height)

        return height
    
    def insert(self, value: int, unique = False):
        """
        Inserts a value into the binary search tree.
        Accepts a parameter, unique: bool, which decides if the tree can only hold unique values
        """
        value_node = TreeNode(value, None, None)

        if self.__root is None or self.size() == 0:
            self.__root = value_node
        else:
            self.__sink(value_node, self.__root)
        
        #increment the size whenever an element is inserted
        self.__size += 1
    
    def __sink(self, value_node: TreeNode, node: TreeNode):

        if node is None:
            raise ValueError
        
        if value_node.value < node.value:
            if node.has_l_child():
                self.__sink(value_node.value, node.left)
            else:
                node.left = value_node
        elif value_node > node.value:
            if node.has_r_child():
                self.__sink(value_node, node.right)
            else:
                node.right = value_node
        else:
            pass
            #Moves an equal value to a left child, if the binary search tree can have duplicates
            #if not self.__unique:
                #if node.has_l_child():
                    #node.left = TreeNode(value, node.left, None)
                #else:
                    #node.left = TreeNode(value, None, None)

    def delete(self, value: int):
        """
        Removes the (first instance of) value (if it has duplicates) from the binary search tree.
        Does not raise an error if the value does not exist.
        """
        if self.__root is None or self.size() == 0:
            return

        node, parent = self.__find(value, self.__root, None)

        if node is None:
            return
        else:
            successor, s_parent = self.__find_successor(node.value, node, parent)
            successor.left = node.left
            s_parent.left = None

            if parent is not None:
                if parent.has_l_child() and node.value == parent.left.value:
                    parent.left = successor
                    
                if parent.has_r_child() and node.value == parent.right.value:
                    parent.right = successor

        #decrement the size whenever an element is inserted
        self.__size -= 1

    def find_successor(self, value: int):
        """
        Returns the successor node.
        If the value is not in the tree, returns None.
        """
        if self.__root is None or self.size() == 0:
            return None

        node, parent = self.__find_successor(value, self.__root, None)

        return node.value

    def __find_successor(self, value: int, node: TreeNode, parent: TreeNode):
        
        if node.value > value:
            if node.has_l_child():
                return self.__find_successor(value, node.left)
            else:
                return (None, None)
        elif node.value < value:
            if node.has_r_child():
                return self.__find_successor(value, node.right)
            else:
                return (None, None)
        else:
            if node.has_r_child():
                return (node.right, parent)
            else:
                return (parent, parent)

    def find_greater_than(self, value: int):
        """
        Returns all values in the tree greater than the value
        """
        list_of_values = []

        upper_bound = self.max() + 1

        list_of_values.extend(self.__in_order_traversal_find(self.__root, value, upper_bound))

        return list_of_values
    
    def find_lesser_than(self, value: int):
        """
        Returns all values in the tree greater than the value
        """
        list_of_values = []

        lower_bound = self.mmin() - 1

        list_of_values.extend(self.__in_order_traversal_find(self.__root, lower_bound, value))

        return list_of_values
    
    def find_between(self, lower_bound: int, upper_bound: int):
        """
        Returns all values in the tree between the upper and lower bounds (not including bounds)
        """
        list_of_values = []

        list_of_values.extend(self.__in_order_traversal_find(self.__root, lower_bound, upper_bound))

        return list_of_values
    
    def __in_order_traversal_find(self, node: TreeNode, lower_bound: int, upper_bound: int):

        list_of_values = []

        if node.value > lower_bound and node.has_l_child():
            list_of_values.extend(self.__in_order_traversal_find(node.left, lower_bound, upper_bound))
        
        if node.value > lower_bound and node.value < upper_bound:
            list_of_values.append(node.value)
        
        if node.value < upper_bound and node.has_r_child():
            list_of_values.extend(self.__in_order_traversal_find(node.right, lower_bound, upper_bound))
        
        return list_of_values

    def find(self, value: int):
        """
        Returns value if the tree has the value, None if not
        """
        if self.__root is None or self.size() == 0:
            return None
        else:
            node, parent = self.__find(value, self.__root, None)

            if node is None:
                return None
            
            return node.value

    def __find(self, value: int, node: TreeNode, parent: TreeNode):

        if node.value == value:
            return (value, parent)
        elif node.value > value:
            if node.has_l_child():
                return self.__find(node.left, node)
            else:
                return (None, None)
        else:
            if node.has_r_child():
                return self.__find(node.right, node)
            else:
                return (None, None)

    def max(self):
        """
        Returns the maximum value in the binary search tree.
        """
        
        if self.__root is None or self.size() == 0:
            return 0
        
        return self.__max(self.__root)
    
    def __max(self, node: TreeNode):

        maximum = node.value

        if node.has_r_child():
            maximum = self.__max(node.right)
        
        return maximum
    
    def min(self):
        """
        Returns the minimum value in the binary search tree.
        """
        
        if self.__root is None or self.size() == 0:
            return 0
        
        return self.__min(self.__root)
    
    def __min(self, node: TreeNode):

        minimum = node.value

        if node.has_l_child():
            minimum = self.__min(node.left)
        
        return minimum