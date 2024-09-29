class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n  
        pos = 0
        neg = 1
        
        for i in range(n):
            if nums[i] < 0:
                arr[neg] = nums[i]
                neg += 2
            else:
                arr[pos] = nums[i]
                pos += 2
                
        return arr 
    

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = 0, 1
        
        while pos < n and neg < n:
            if nums[pos] > 0:
                pos += 2
            elif nums[neg] < 0:
                neg += 2
            else:
                nums[pos], nums[neg] = nums[neg], nums[pos]
        
        return nums

# Example usage
sol = Solution()
example_input = [3, 1, -2, -5, 2, -4]
result = sol.rearrangeArray(example_input)
print("Rearranged array:", result)
