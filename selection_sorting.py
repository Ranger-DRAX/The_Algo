
"""
time complexity to O(n^2)
"""
def selection_sorting(arr):
    for x in range(len(arr)):

        min_idx=x
        for y in range(x+1,len(arr)):
            if arr[min_idx] > arr[y]:
                min_idx=y
        arr[x],arr[min_idx]=arr[min_idx],arr[x]
    return arr
print(selection_sorting([89,47,551,245,2,54,8878,48,8,777]))


