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

    def subtree_first(self):
        #finding the first node in the subbtree  git 
        if self.left: return self.left.subtree_first()
        else: return self
    
    def subtree_last(self):
        # finding the last node in the subtree 

        if self.right: return self.right.subtree_first()
        else: return self

# tree succesor or predecessor
    def successor(self):
        if self.right: return self.right.subtree_first()
        while self.parent and (self is self.parent.right):
            self =self.parent
        return self.parent
    def predecessor(self):
        if self.left:  return self.left.subtree_first()
        while self.parent and (self is self.parent.left):
            self =self.parent
        return self.parent
    
#Dynamic operations 
#Insert inside a Tree
    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right. B.parent = B,A
        else:
            A.left, B.parent = B, A
    
    def subtree_insert_after(A,B):
        if A.right:
            A = A.right.subtree_first ()
            A.left, B.parent = B, A
        else:
            A.right, B.parent =B, A
