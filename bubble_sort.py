"""
time complexity to O(n^2)
"""

from bigO import BigO
from bigO import algorithm

def bubble_sort(arr):

    for x in range(len(arr)):
        for y in range(len(arr)-1):
            if arr[y]>arr[y+1]:
                arr[y],arr[y+1]=arr[y+1],arr[y]

    return arr
print(bubble_sort([2,8,5,3,9,4,1]))

lib = BigO(bubble_sort)


lib.test(bubble_sort, "random")
lib.test_all(bubble_sort)
lib.runtime(bubble_sort, "random", 5000)
lib.runtime(algorithm.insertSort, "reversed", 32)
lib.compare(algorithm.insertSort, algorithm.bubbleSort, "all", 5000)