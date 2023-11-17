"""
list should be sorted
time complexity to O(log N)
"""
def binary_search(arr,target):
    low=0
    high=len(arr)-1


    while low<= high:
        mid = (low + high) // 2
        if  arr[mid]==target:
            return f"found it on {mid} position"
        elif arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1

    return f"not found 🐸"
sorted_list=[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(binary_search(sorted_list,5))
print(binary_search(sorted_list,52))
print(binary_search(sorted_list,72))