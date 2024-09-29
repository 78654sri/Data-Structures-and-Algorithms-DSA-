def cntSubarrays(arr, target_sum):
    prev_sum = {}  # Dictionary to store cumulative sum frequencies
    res = 0  # To store the count of subarrays
    curr_sum = 0  # Cumulative sum initialized to 0
    
    for num in arr:
        curr_sum += num  # Update cumulative sum
        
        # If the cumulative sum equals target_sum, increment the result
        if curr_sum == target_sum:
            res += 1
        
        # Check if (curr_sum - target_sum) exists in prev_sum
        if (curr_sum - target_sum) in prev_sum:
            res += prev_sum[curr_sum - target_sum]
        
        # Update the dictionary with the current cumulative sum
        if curr_sum in prev_sum:
            prev_sum[curr_sum] += 1
        else:
            prev_sum[curr_sum] = 1
    
    return res  # Return the count of subarrays
arr = [10, 2, -2, -20, 10]
target_sum = -10
