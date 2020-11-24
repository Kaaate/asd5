from random import randint
import time

from Sortings.shell_sort import shell_sort
from Sortings.heap_sort import heap_sort
from Sortings.merge_sort import merge_sort
from Sortings.quick_sort import quick_sort

def generateRandomArray(size):
    data = []
    for _ in range(0, 10**size):
        data.append(randint(-20, 20))
    return data

print("#BLOCK 1#\n")
for i in [4,5,6]:
    data = generateRandomArray(i)
    print(f"{10**i} elements:")

    start = time.time()
    shell_sort(data.copy())
    print(f"Shell sort: {round((time.time()-start)*1000,3)} ms.")

    start = time.time()
    merge_sort(data)
    print(f"Merge sort: {round((time.time()-start)*1000, 3)} ms.")

    start = time.time()
    quick_sort(data.copy())
    print(f"Quick sort: {round((time.time()-start)*1000,3)} ms.")

    start = time.time()
    heap_sort(data)
    print(f"Heap sort: {round((time.time()-start)*1000, 3)} ms.\n")

print("#BLOCK 2#\n")
for i in [4,5,6]:
    data = list(range(0,10**i))

    print(f"{10**i} elements:")

    start = time.time()
    shell_sort(data)
    print(f"Shell sort: {round((time.time()-start)*1000,3)} ms.")

    start = time.time()
    heap_sort(data)
    print(f"Heap sort: {round((time.time()-start) * 1000, 3)} ms.")

    start = time.time()
    quick_sort(data.copy())
    print(f"Quick sort: {round((time.time() - start) * 1000, 3)} ms.")

    start = time.time()
    heap_sort(data)
    print(f"Heap sort: {round((time.time() - start) * 1000, 3)} ms.\n")