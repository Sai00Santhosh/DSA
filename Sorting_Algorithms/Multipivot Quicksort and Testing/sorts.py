import sys
sys.setrecursionlimit(1500)


def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

####################################################################################

def quicksort_inplace(a, low=0, high=None):
    
    if high == None:
        high = len(a) - 1
    if low < high:
        p_idx = partition(a,low,high)
        quicksort_inplace(a, low, p_idx - 1)
        quicksort_inplace(a, p_idx + 1, high)
        
    return a
    
def partition(a, low, high):
    i = low - 1
    pivot = a[high]
    for j in range(low,high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

####################################################################################

def dual_pivot_quicksort(list):
    n = len(list)
    if n <= 1:
        return list
    elif n == 2:
        return sorted(list)
    pivot1, pivot2 = sorted([list.pop(0), list.pop(0)])
    a = []
    b = []
    c = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        else:
            c.append(element)
    return dual_pivot_quicksort(a) + [pivot1] + dual_pivot_quicksort(b) + [pivot2] + dual_pivot_quicksort(c)

####################################################################################

def tri_pivot_quicksort(list):
    n = len(list)
    if n <= 1:
      return list
    elif n == 2:
        return sorted(list)
    pivot1, pivot2, pivot3 = sorted([list.pop(0), list.pop(0), list.pop(0)])
    a = []
    b = []
    c = []
    d = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        elif pivot2 <= element < pivot3:
            c.append(element)
        else:
            d.append(element)
    return (tri_pivot_quicksort(a) + [pivot1] + tri_pivot_quicksort(b) + 
            [pivot2] + tri_pivot_quicksort(c) + [pivot3] + tri_pivot_quicksort(d))

####################################################################################
    
def quad_pivot_quicksort(list):
    n = len(list)
    if n <= 1:
        return list
    elif n == 2 or n == 3:
        return sorted(list)
    pivot1, pivot2, pivot3, pivot4 = sorted([list.pop(0), list.pop(0), list.pop(0),
    list.pop(0)])
    a = []
    b = []
    c = []
    d = []
    e = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        elif pivot2 <= element < pivot3:
            c.append(element)
        elif pivot3 <= element < pivot4:
            d.append(element)
        else:
            e.append(element)
    return (quad_pivot_quicksort(a) + [pivot1] 
    + quad_pivot_quicksort(b) + [pivot2] + 
    quad_pivot_quicksort(c) + [pivot3] + quad_pivot_quicksort(d) + [pivot4] + quad_pivot_quicksort(e))

# Python3 program to implement

####################################################################################

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        
    return arr
        
####################################################################################
        
def selection_sort(array):
    
    size = len(array)
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])
        

####################################################################################
        
def bubblesort(L):  
    n = len(L)
    swap = True
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swap = True
        if not swap:
            break
    return L
    
####################################################################################
        
def final_sort(list):
    
    n = len(list)
    if n <= 1:
        return list
    elif n <= 10:
        return insertion_sort(list)
    pivot1, pivot2, pivot3, pivot4 = sorted([list.pop(0), list.pop(0), list.pop(0),
    list.pop(0)])
    a = []
    b = []
    c = []
    d = []
    e = []
    for element in list:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element < pivot2:
            b.append(element)
        elif pivot2 <= element < pivot3:
            c.append(element)
        elif pivot3 <= element < pivot4:
            d.append(element)
        else:
            e.append(element)
    
    return (final_sort(a) + [pivot1] 
    + final_sort(b) + [pivot2] + 
    final_sort(c) + [pivot3] + final_sort(d) + [pivot4] + final_sort(e))
                
####################################################################################
            



