def second_largest_element(arr):
    if len(arr) < 2:
        return None  

    max_val = arr[0]
    second_largest = -1

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            second_largest = max_val
            max_val = arr[i]
        elif arr[i] > second_largest and arr[i] < max_val:
            second_largest = arr[i]

    return second_largest

arr = [3, 1, 4, 4, 5, 2]
result = second_largest_element(arr)
print("The second largest element is:", result)  # Output: 4

"""==============================================================================="""

def second_largest_element(arr):
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i

    second_largest = -1
    for i in arr:
        if i > second_largest and i != max_val:
            second_largest = i

    return second_largest
arr = [3, 1, 4, 4, 5, 2]
result = second_largest_element(arr)
print("The second largest element is:", result) 

"""==============================================================================="""
