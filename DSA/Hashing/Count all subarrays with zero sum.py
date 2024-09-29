def findSubarray(arr, n):
    map = {}
    sum_val = 0
    count = 0
    
    for i in range(n):
        sum_val += arr[i]
        
        if sum_val == 0:
            count += 1
        
        if sum_val in map:
            count += map[sum_val]
        
        map[sum_val] = map.get(sum_val, 0) + 1
    
    return count

# Example usage:
arr = [2, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(findSubarray(arr, n)) 