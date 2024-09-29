from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_count = count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
  
    max_count = max(max_count, count)
    return max_count


nums = [1, 1, 0, 1, 1, 1]
result = findMaxConsecutiveOnes(nums)
print(result)  # Output: 3
