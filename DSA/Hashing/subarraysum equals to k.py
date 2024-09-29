def countSubarraysWithSumK(a, K):
    n = len(a)
    count = 0
    
    for i in range(n):
        for j in range(i, n):
            sum_val = 0
            for k in range(i, j + 1):
                sum_val += a[k]
            
            if sum_val == K:
                count += 1
    
    return count

# Example usage:
a = [1, 2, 3, 4, 5]
K = 6
print(countSubarraysWithSumK(a, K)) 





def subarraySum(nums, k):
    answer = 0
    prefix_sum = 0
    memo = {}
    memo[0] = 1
    n = len(nums)
    
    for i in range(n):
        prefix_sum += nums[i]
        
        if prefix_sum - k in memo:
            answer += memo[prefix_sum - k]
        
        memo[prefix_sum] = memo.get(prefix_sum, 0) + 1
    
    return answer

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 5
print(subarraySum(nums, k)) 