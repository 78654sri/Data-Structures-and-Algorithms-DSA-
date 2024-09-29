from collections import defaultdict

class Solution:
    def maxOperations(self, nums, target):
        hmap = defaultdict(int)
        count = 0
        
        for num in nums:
            complement = target - num
            if hmap[complement] > 0:
                count += 1
                hmap[complement] -= 1
            else:
                hmap[num] += 1
        
        return count

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 1,3, 3, 4, 3]
    target = 6
    result = solution.maxOperations(nums, target)
    print(result)  # Output should be 1, since we can form one pair (3, 3) to sum to 6.
