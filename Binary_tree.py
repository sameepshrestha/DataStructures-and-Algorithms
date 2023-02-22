class Binary_Node:
    def __init__(self,x):
        self.item = x
        self.right = None
        self.left = None
        self.parent=None

    def subtree_iter(self):
        if self.left: yield from self.left.subtree_iter()
        yield self
        if self.right: yield from self.right.subtree_iter()

#tree navigation 

