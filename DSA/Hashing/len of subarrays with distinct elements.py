
def sum_of_length(arr):
    s = set()  # To store distinct elements
    j = 0  # Right pointer
    ans = 0  # To store the final answer
    n = len(arr)  # Length of the array
    
    for i in range(n):  # Left pointer
        while j < n and arr[j] not in s:  # Expand the window as long as the element is distinct
            s.add(arr[j])
            j += 1
        
        # The number of valid subarrays ending at index j-1 that start from index i is (j - i)
        ans += ((j - i) * (j - i + 1)) // 2
        
        # Shrink the window by removing the element at the start (i) of the current window
        s.remove(arr[i])
    
    return ans
arr=[1,2,3,2,4]
result=sum_of_length(arr)
print(result)