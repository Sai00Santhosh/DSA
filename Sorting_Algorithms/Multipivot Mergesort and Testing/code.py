import sys

from sorts import *
sys.path.append("..")

import random
import timeit
import math
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(1500)

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

####################################################################################

# plot for quad_pivot_quicksort()
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
        build_heap1(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='mergesort() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of mergesort()")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

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
        mergesort_bottom(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='mergesort_bottom() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of mergesort_bottom()")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

ns = [10*i for i in range(100)]
ts = []

runs = 10
for n in ns:
    arr = create_random_list(n)
    for _ in range(runs):
        start = timeit.default_timer()
        mergesort_three(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(ns, ts, '.', label='mergesort_three() running time')
plt.xlabel("array length (n)")
plt.ylabel("time (t)")
plt.title("measure the performance of mergesort_three()")
plt.legend(loc = "upper left")
    
plt.show()


####################################################################################

####################################################################################
#WORST CASE EXPERIMENT
####################################################################################

####################################################################################

factors = np.linspace(0,0.5,1000)
ts = []

runs = 100
for n in factors:
    total = 0
    arr = create_near_sorted_list(100, n)
    for _ in range(runs):
        start = timeit.default_timer()
        mergesort_bottom(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(factors, ts, '.', label='mergesort_bottom() @ list length = 100')
plt.xlabel("factor")
plt.ylabel("time (t)")
plt.title("measure the performance of mergesort_bottom() random case")
plt.legend(loc = "upper left")
    
plt.show()

####################################################################################

factors = np.linspace(0,0.5,1000)
ts = []

runs = 100
for n in factors:
    total = 0
    arr = create_random_list(100)
    for _ in range(runs):
        start = timeit.default_timer()
        mergesort_bottom(arr)
        end = timeit.default_timer()
        total += (end - start)
    ts.append(total / runs)
plt.plot(factors, ts, '.', label='mergesort_bottom() @ list length = 100X')
plt.xlabel("factor")
plt.ylabel("time (t)")
plt.title("measure the performance of mergesort_bottom() worst-case")
plt.legend(loc = "upper left")
    
plt.show()