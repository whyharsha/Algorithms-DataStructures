class TreeNode():
    """
    Implements a node for a binary search tree - value, left and right children
    """

    def __init__(self, value: int, left: TreeNode, right: TreeNode):
        self.value = value
        self.left = left
        self.right = right
        
    def has_l_child(self):
        return (self.left is not None)
    
    def has_r_child(self):
        return (self.right is not None)