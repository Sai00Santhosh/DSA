import math

class k_heap:
    length = 0
    data = []
    
    def __init__(self, values, k):
        if not isinstance(k, int) or k <= 1:
            raise ValueError("Degree of K-ary heap (n) must be an integer > 1")
        self._k = k
        self.data = values
        self.length = len(values)
        self.build_heap(self._k)
        
    def build_heap(self, k):
        for i in range(self.length // k - 1, -1, -1):
            self.sink(i)
        
    def parent(self, i):
        return math.ceil(i / self._k) - 1
        
    def children(self, i):
        first = i * self._k + 1
        list1 = list(range(first, min(first + self._k, len(self.data))))
        return list1
        
    def sink(self, i):
        largest_known = i
        for j in range(0, self._k):
            if self.child(j, i) < self.length and self.data[self.child(j, i)] > self.data[i]:
                if self.data[self.child(j, i)] > self.data[largest_known]:
                    largest_known = self.child(j, i)
        if largest_known != i: 
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)
            
    #helper functions
    
    def child(self, k, i):
        return self._k * i + 1 + k