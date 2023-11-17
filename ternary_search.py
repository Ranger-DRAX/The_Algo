"""
https://www.youtube.com/shorts/AI9Rqd9qY1g?feature=share
"""
def ternary_search(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid_1=low + (high-low)//3
        mid_2=high-(high-low)//3

        if target==arr[mid_1]:
            return f"found it on position {mid_1}"
        if target==arr[mid_2]:
            return f"found it on position {mid_2}"

        if target<arr[mid_1]:
            high=mid_1-1
        elif target>arr[mid_2]:
            low=mid_2+1
        else:
            low=mid_1+1
            high=mid_2-1
    return f"not found 🐸"
list=[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(ternary_search(list,91))
