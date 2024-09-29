# Finding Maximum Subarray Sum

#Brute force
def maximum_subarray(arr):
    max_sum = float("-inf")
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            actual_sum = 0
            for k in range(i, j+1):
                actual_sum += arr[k]
            max_sum = max(max_sum, actual_sum)
    return max_sum
#Better												
 def maximum_subarray(arr):
    max_sum = float("-inf")
    for i in range(len(arr)):
        cumulative_sum = 0
        for j in range(i, len(arr)):
            cumulative_sum += arr[j]
            max_sum = max(max_sum, cumulative_sum)
    return max_sum

#Kandeys algorithm
def maximum_subarray(arr):
    global_sum = float("-inf")
    local_sum = 0
    for elem in arr:
        local_sum = max(elem, local_sum+elem)
        global_sum = max(global_sum, local_sum)
    return global_sum
