import random
"""
The most basic searching algorithm
Given an item to search from a bucket of items, we search ONE BY ONE.
If we find then bingo! Else we look till the end of bucket.

"""

def linear_search(arr,target):
    for x in range(len(arr)):
        if arr[x]==target:
            return f"found it at position: {x} "
    return "Not found"



# Generate a list of 10 random integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(100)]

target=69

print(linear_search(numbers,target))
