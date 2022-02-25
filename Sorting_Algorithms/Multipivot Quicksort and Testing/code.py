import sys

from sorts import *
sys.path.append("..")

import random
import timeit
import math
import matplotlib.pyplot as plt

sys.setrecursionlimit(1500)

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

####################################################################################
# plot for quicksort_inplace()
ns = [10*i for i in range(100)] 
ts = []

runs = 10
for n in ns:
    arr = create_random_list(n)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        quicksort_inplace(arr, l, h)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='quicksort_inplace() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of quicksort_inplace()")
plt.legend(loc = "upper left")
    
plt.show()
####################################################################################

# plot for my_quicksort()
ns = [10*i for i in range(100)]
ts = []

runs = 10
for n in ns:
    arr = create_random_list(n)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        my_quicksort(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='my_quicksort() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of my_quicksort()")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

# plot for dual_pivot_quicksort()
ns = [10*i for i in range(100)]
ts = []

runs = 10
for n in ns:
    arr = create_random_list(n)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        dual_pivot_quicksort(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='dual_pivot_quicksort() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of dual_pivot_quicksort()")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

# plot for tri_pivot_quicksort()
ns = [10*i for i in range(100)]
ts = []

runs = 10
for n in ns:
    arr = create_random_list(n)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        tri_pivot_quicksort(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='tri_pivot_quicksort() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of tri_pivot_quicksort()")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

# plot for quad_pivot_quicksort()
ns = [10*i for i in range(100 )]
ts = []

runs = 10
for n in ns:
    arr = create_random_list(n)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        quad_pivot_quicksort(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='quad_pivot_quicksort() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of quad_pivot_quicksort()")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

# plot for final_sort()
ns = [10*i for i in range(100)]
ts = []

runs = 10
for n in ns:
    arr = create_random_list(n)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        final_sort(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='final_sort() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of final_sort()")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

# Worst Case Question experimentation area below

ns = [10*i for i in range(100)]
ts = []

runs = 10
for n in ns:
    arr = create_near_sorted_list(n, 100)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        my_quicksort(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='my_quicksort() running time on near sorted lists - factor 100')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of my_quicksort()")
plt.legend(loc = "upper left")
    
plt.show()

### INSERTION SORT GRAPH

ns = [10*i for i in range(100)]
ts = []

runs = 10
for n in ns:
    arr = create_near_sorted_list(n, 100)
    l = 0
    h = len(arr) - 1
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        insertion_sort(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='insertion_sort() running time on near sorted lists - factor 100')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of insertion_sort()")
plt.legend(loc = "upper left")
    
plt.show()