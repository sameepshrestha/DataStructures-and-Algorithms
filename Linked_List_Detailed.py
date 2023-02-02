#you have to have a separate node class for building the linked list
class Node:
    def __init__(self,x):
        self.item = x
        self.next =None

class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def __len__(self): return self.size 
    #storing the size make it efficient to call anytime

    def __iter__(self):
        node=self.head
        while node:
            yield node.item
            node=node.next

    def build(self,X):
        for a in reversed(X):
            self.insert_first(a)
   
    def later_node(self,i):
        if i==0:return self
        assert self.next
        return self.later_node(i-1)

    def get_at(self,i):
        node = self.head.later_node(i)
        return node.item 

    def set_at(self,i,x):
        node = self.head.later_node(i)
        node.item =x
        
    def insert_first(self,X):
        new_node = Node(X)
        new_node.next = self.head
        self.head =new_node

    def insert_at(self,i,X):
        if i==0:
            self.insert_first(X)
        new_node =X
        node = self.head.later_node(i-1)
        new_node.next =node.next
        node.next = new_node
        self.size+=1
 

a = LinkedList()
a.build(["Mon"])
print(a.get_at(0))
a.insert_first("tue")
print(a.get_at(0))
