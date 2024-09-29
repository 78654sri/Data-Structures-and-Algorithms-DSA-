def reverse_array_extra_array(arr):
    reversed_arr = arr[::-1]

    # Print reversed array
    print("Reversed Array:", end=" ")
    for i in reversed_arr:
        print(i, end=" ")

# Example usage:
original_arr = [1, 2, 3, 4, 5]
reverse_array_extra_array(original_arr)

# Iterative python program to reverse an array

# Function to reverse A[] from start to end


"""==============================================================================="""
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
# This program is contributed by Pratik Chhajer

"""==============================================================================="""
original_array = [1, 2, 3, 4, 5]

# Using inbuilt method in Python
reversed_array = list(reversed(original_array))

# Print the reversed array
print(reversed_array)


# Recursive python program to reverse an array

# Function to reverse A[] from start to end


"""==============================================================================="""
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)


# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
# This program is contributed by Pratik Chhajer

"""==============================================================================="""
def reverse_array_using_stack(arr):
    stack = []
    
    # Push elements onto the stack
    for element in arr:
        stack.append(element)
    
    # Pop elements from the stack to reverse the array
    for i in range(len(arr)):
        arr[i] = stack.pop()

# Example usage:
arr = [1, 2, 3, 4, 5]
reverse_array_using_stack(arr)
print("Reversed Array:", arr)
