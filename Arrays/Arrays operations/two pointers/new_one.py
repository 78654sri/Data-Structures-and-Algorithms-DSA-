def clone_even_numbers(a):
    if a is None:
        return None
    
    # Find the last non-None number in the array
    def find_last_number(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] is not None:
                return i
        return -1

    i = find_last_number(a)
    end = len(a)

    # Process the array from the end to the beginning
    while i >= 0:
        if a[i] % 2 == 0:
            end -= 1
            a[end] = a[i]  # Clone even number
            end -= 1
            a[end] = a[i]  # Second copy of the even number
        else:
            end -= 1
            a[end] = a[i]  # Copy the odd number
        
        i -= 1
    
    return a

# Example usage
a = [2, 3, 5, 8, None, None, None, None]
result = clone_even_numbers(a)
print(result)