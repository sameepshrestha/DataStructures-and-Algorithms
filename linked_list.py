class Linked_list:
    def __init__(self,x):
        self.item= x
        self.next = None
    def later_node(self,i):
        #recursive implementation (here the instance change but the value differs)
        if i==0: return self
        assert self.next #chefcking if there is the next item
        return self.next.later_node(i-1)