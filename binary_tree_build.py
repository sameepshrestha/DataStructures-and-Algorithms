""""Exercise: Given an array of items A = (a0, . . . , an−1), describe a O(n)-time algorithm to 
construct a binary tree T containing the items in A such that (1) the item stored in the i
th node of T’s traversal order is item ai, and (2) T has height O(log n).""""

#flow chart 
"""
Step 1 : Finding the length of an array, which would  take O(1) time complexity 
the root as the middle term:"""
def build(A):
    # length = len(arr)
    def build_subtree(A,i,j):
        c = i+j//2
        root  = self.Node_Type(A[c])
        if i<c:
            root.left = build_subtree(A,i,c-1)
            root.left.parent = root
        if c<j:
            root.right = build_subtree(A,c+1,j)
            root.right.parent =root
        return root
    self.root =build_subtree(A,0,len(A)-1)

""" lets break this algorithm for an exmple shall we :
for an array A =[0,1,2,3,4,5,6]
step1: call function with (array,i,j) which is (A,0,6)
step2: c= 3 : so the node is generated as root=A[3]\
step3: since 0<3, we have A[3].left which calls the function again with (A,0,2)
step4: c =1 so a node is generated as root =A[1] and since 0<1 we have another call for A[1].left with (A,0,0)
step5: c = 0 since i not less than c and c not less than j we return A[0], which thus becomes A[1].left=A[0]
step6: we return back to function call with (A,0,2) with root =A[1]
step6: we have c<j so we determine A[1].right and again call the function with (A,2,2)
step7: since none fo the condition is called and the root is A[2] we return A[2] which is assigned to A[1].right
#here we have our first subtree with 1 as parent and  0 as left leaf and 2 as right leaf which maintains the traversal order given
, now we continue the recursion to complete the recursion steps"""
