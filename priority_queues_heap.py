class PriorityQueue:
    def __init__(self):
        self.A=[]

    def insert(self,x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) <1:
            raise  IndexError("Pop from empty priority queue")
        return self.A.pop()

    @classmethod
    def sort(Queue,A):
        pq=Queue()
        for x in A:
            pq.insert(x)
        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out

#binary heap implementation 

class PQHeap(PriorityQueue):
    def insert(self, x):
        super().insert(x)
        n,A =self.n, self.A
        max_heapify_up(A,n,n-1)


    def delete_max(self):
        n,A =self.n, self.A
        A[0],A[n]= A[n], A[0]
        max_heapify_down(A, n, 0)
        return super().delete_max()
    
    def parent(i):
        p = (i-1)//2
        return p if 0<i  else i 
    
    def left(i,n):
        l= 2*i +1
        return l if l<n else i 

    def right(i,n):
        r= 2*i+2
        return r if r<n else i 
    
    def max_heapify_up(A,n,c):
        p = parent(c)
        if A[p] < A[c]:
            A[p], A[c] = A[c],A[p]
            max_heapify_up(A,n,p)

    def max_heapify_down(A,n,p):
        l, r =left(p,n), right(p,n) 
        c = l if A[l] > A[r] else r 
        if A[p]< A[c]:
            A[p], A[c] = A[c],A[p]
            max_heapify_down(A,n, c)

    def build_max_heap(A):
        n= len(A)
        for i in range(n//2, -1, -1):
            max_heapify_down(A, n -1)
        