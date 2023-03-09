class Binary_Node:
    def __init__(A,x):
        A.item = x
        A.right = None
        A.left = None
        A.parent=None

    def subtree_iter(A):
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

#tree navigation 

    def subtree_first(A):

        #finding the first node in the subbtree  git 
        if A.left: return A.left.subtree_first()
        else: return A
    
    def subtree_last(A):
        # finding the last node in the subtree 

        if A.right: return A.right.subtree_first()
        else: return A

# tree succesor or predecessor
    def successor(A):
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A =A.parent
        return A.parent
    
    def predecessor(A):
        if A.left:  return A.left.subtree_first()
        while A.parent and (A is A.parent.left):
            A =A.parent
        return A.parent
    
#Dynamic operations 
#Insert inside a Tree
    def subtree_insert_before(A, B):

        """ Inserting in a tree, we must preserve the traversal order, thus to enter before, if the node
        does not have a left node we enter the value there or if there is a left node than we determine 
        the last node in the subree and insert at the right of the node"""
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B,A
        else:
            A.left, B.parent = B, A
    
    def subtree_insert_after(A,B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent =B, A

# Delete inside a tree 

    def subree_delete(A):
        if A.left or A.right:
            """ preserving the traversal order by going through the predecessor and sucessor to make the node
            to be deleted into a node so that we can remove it easily"""
            if A.left: B=A.predecessor()
            else: B= A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            # just deleting the left and keeping the nodes leaves as none
            if A.parent.left is A: A.parent.left= None
            else: A.parent.right = None
        return A

class Binary_Tree:
    def __init__(T, Node_type =  Binary_Node):
        T.rot = None
        T.size = 0 
        T.Node_Type = Node_type

    def __len__(T): return T.size
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item
    
