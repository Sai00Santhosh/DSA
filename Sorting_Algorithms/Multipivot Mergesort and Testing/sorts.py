import sys
sys.setrecursionlimit(1500)


####################################################################################

def merge_bottom(L, temp, start, mid, end):
 
    k = start
    i = start
    j = mid + 1
 
    while i <= mid and j <= end:
        if L[i] < L[j]:
            temp[k] = L[i]
            i = i + 1
        else:
            temp[k] = L[j]
            j = j + 1
 
        k = k + 1
 
    while i < len(L) and i <= mid:
        temp[k] = L[i]
        k = k + 1
        i = i + 1
 
    for i in range(start, end + 1):
        L[i] = temp[i]
 
 
def mergesort_bottom(L):
 
    low = 0
    high = len(L) - 1

    temp = L.copy()

    m = 1
    while m <= high - low:
 
        for i in range(low, high, 2*m):
            start = i
            mid = i + m - 1
            end = min(i + 2*m - 1, high)
            merge_bottom(L, temp, start, mid, end)
 
        m = 2*m

####################################################################################   
        
def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L

#################################################################################### 

def merge_three(left, middle, right):
    
    L = []
    i = j = k = 0
    while i < len(left) and j < len(right) and k < len(middle):
        if left[i] < right[j]:
            if left[i] < middle[k]:
                L.append(left[i])
                i += 1
            else:
                L.append(middle[k])
                k += 1
        elif right[j] < middle[k]:
            L.append(right[j])
            j+=1
        else:
            L.append(middle[k])
            k += 1

    while j < len(right) and k < len(middle):
        if right[j] < middle[k]:
            L.append(right[j])
            j+=1
        else:
            L.append(middle[k])
            k+=1

    while i < len(left) and k < len(middle):
        if left[i] < middle[k]:
            L.append(left[i])
            i+=1
        else:
            L.append(middle[k])
            k+=1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L.append(left[i])
            i+=1
        else:
            L.append(right[j])
            j+=1

    while i < len(left):
        L.append(left[i])
        i+=1

    while j < len(right):
        L.append(right[j])
        j+=1

    while k < len(middle):
        L.append(middle[k])
        k+=1

    return L


def mergesort_three(array):
    if len(array) < 2:
        return array

    if len(array) == 2:

        if(array[0] > array[1]):
            temp = array[0]
            array[0] = array[1]
            array[1] = temp
        return array
    
    r = len(array) // 3
    h = len(array) % 3

    left = mergesort_three(array [:r])

    middle = mergesort_three(array[(r):((2*r+1))])

    right = mergesort_three(array[((2*r+1)):((3*r)+h)])

    return merge_three(left, middle, right)
