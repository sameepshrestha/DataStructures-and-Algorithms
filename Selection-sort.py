class Selectionsort:
    def __init__(self,array):
        self.array=array
    def sort(self):
        for i in range(len(self.array),0,-1):
            m = i
            for j in range(j):
                if self.array[m]<self.array[j]:
                    m=j
            self.array[m],self.array[i]=  self.array[i],self.array[m]   
    
