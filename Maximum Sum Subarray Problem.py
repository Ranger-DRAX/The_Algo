# brute force approach
"""
Time complexity: O(n^2 )
"""

def max_subarray_sum(arr):#
    n=len(arr)
    max_sum=arr[0]
    for x in range(n):
        current_sum=0
        for y in range(x,n):
            current_sum+=arr[y]
            if current_sum > max_sum :
                max_sum=current_sum
    return  max_sum

print(max_subarray_sum([10,1,-3,4,-1,2,1,-5,40]))
