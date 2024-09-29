from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        index = n - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                nums[index] = nums[left] ** 2
                left += 1
            else:
                nums[index] = nums[right] ** 2
                right -= 1
            index -= 1
        
        return nums

# Example usage
sol = Solution()
example_input = [-7, -3, 2, 3, 11]
result = sol.sortedSquares(example_input)
print("Squared and sorted array:", result)


from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        index = n - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
            index -= 1
        
        return result

# Example usage
sol = Solution()
example_input = [-7, -3, 2, 3, 11]
result = sol.sortedSquares(example_input)
print("Squared and sorted array:", result)






def find_v_shape_min(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        if arr[left] > arr[right]:
            # Move left pointer to the right
            left += 1
        else:
            # Move right pointer to the left
            right -= 1
            
    # When left == right, that is the minimum point
    return arr[left]

# Example usage
v_shaped_array = [9, 7, 5, 6, 8]
min_value = find_v_shape_min(v_shaped_array)
print(f"The minimum value in the V-shaped array is: {min_value}")
