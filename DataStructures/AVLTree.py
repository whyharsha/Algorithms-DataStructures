from DataStructures.TreeNode import TreeNode
import math

class AVLTreeNode(TreeNode):
    """
    Implements a node for an AVL tree - value, left and right children, parent
    """

    def __init__(self, value: int, left: AVLTreeNode, right: AVLTreeNode, parent: AVLTreeNode):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def has_l_child(self):
        return (self.left is not None)
    
    def has_r_child(self):
        return (self.right is not None)

class AVLTree(object):
    """
    A tree that keeps itself balanced.
    Balanced trees offer better complexity metrics for various operations.
    """

    def __init__(self):
        self.__root = AVLTreeNode(0, None, None)
        self.__size = 0
    
    def __init__(self, root: AVLTreeNode):

        if root is None:
            raise ValueError

        self.__root = root
        self.__size = 0
    
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
    
    def height(self):
        """
        Computes and returns the height of the tree.
        """
        if self.__root is None or self.size() == 0:
            return 0
        else:
            return self.__height(self.__root, 0)
    
    def __height(self, node: AVLTreeNode, current_height: int):
        height = current_height + 1
        l_height, r_height = height, height

        if node.has_l_child():
            l_height = self.__height(node.left, l_height)
        
        if node.has_r_child():
            r_height = self.__height(node.right, r_height)
        
        if height < max(l_height, r_height):
            height = max(l_height, r_height)

        return height

    def insert(self, value: int):
        """
        Adds a value into the tree.
        """
        if self.__root is None or self.size() == 0:
            self.__root = AVLTreeNode(value, None, None, None)
        else:
            self.__sink(value, self.__root, None)
        
        self.__size += 1
    
    def __sink(self, value: int, node: AVLTreeNode):

        if value > node.value:
            if node.has_r_child():
                self.__sink(value, node.right)
            else:
                node.right = AVLTreeNode(value, None, None, node)
                self.__check_balance(node)
        elif value < node.value:
            if node.has_l_child():
                self.__sink(value, node.left)
            else:
                node.left = AVLTreeNode(value, None, None, node)
                self.__check_balance(node)
        else:
            pass

    def __balance_factor(self, node: AVLTreeNode):
        l_height, r_height = 0 , 0

        if node.has_l_child():
            l_height = self.__height(node.left, l_height)

        if node.has_r_child():
            r_height = self.__height(node.right, r_height)

        return l_height - r_height
    
    def __check_balance(self, node: AVLTreeNode):
        
        if math.abs(self.__balance_factor(node)) > 1:
            self.__rebalance(node)
        
        if node.parent is not None:
            self.__check_balance(node.parent)
    
    def __rebalance(self, node: AVLTreeNode):

        if self.__balance_factor(node) > 1:
            if self.__balance_factor(node.left) < 0:
                self.__left_rotate(node.left)
                self.__right_rotate(node)
            else:
                self.__right_rotate(node)

        elif self.__balance_factor(node) < -1:
            if self.__balance_factor(node.right) > 0:
                self.__right_rotate(node.right)
                self.__left_rotate(node)
            else:
                self.__left_rotate(node)

        else:
            pass
    
    def __left_rotation(self, node: AVLTreeNode):

        #assign the node's right child as the child of the node's current parent
        parent = node.parent

        if parent is None:
            self.__root = node.right
        else:
            if parent.has_l_child() and parent.left.value == node.value:
                parent.left = node.right
            
            if parent.has_r_child() and parent.right.value == node.value:
                parent.right = node.right
        
        #assign the node's right child as it's parent
        node.parent = node.right

        if node.right.left is None:
            #assign the node as the left child of it's right child
            node.right.left = node
            node.right = None
        else:
            temp = node.right.left
            node.right.left = node
            node.right = temp
    
    def __right_rotation(self, node: AVLTreeNode):

        #assign the node's left child as the child of the node's current parent
        parent = node.parent

        if parent is None:
            self.__root = node.left
        else:
            if parent.has_l_child() and parent.left.value == node.value:
                parent.left = node.left
        
            if parent.has_r_child() and parent.right.value == node.value:
                parent.right = node.left

        #assign the node's left child as it's parent
        node.parent = node.left

        if node.left.right is None:
            #assign the node as the right child of it's left child
            node.left.right = node
            node.left = None
        else:
            temp = node.left.right
            node.left.right = node
            node.left = temp