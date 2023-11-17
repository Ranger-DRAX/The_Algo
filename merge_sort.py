"""
Merge Sort is a popular sorting algorithm that follows the "divide and conquer" strategy
In-Place Merge Sort Algorithm
time complexity to O(nlogn)
"""

def merge_sort(arr):
    if len(arr) > 1:
        left_half = arr[:len(arr) // 2]
        right_half = arr[len(arr) // 2:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):


            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k +=1

        while i < len(left_half):

            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


    return  arr

print(merge_sort([2,6,5,1,7,4,3]))