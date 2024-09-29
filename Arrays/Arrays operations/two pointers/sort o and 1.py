# `from typing import List

# def MoveOnesAtEnd(nums: List[int]) -> int:
#     i=0
#     n=len(nums)
#     for j in range(1,n):
#         if nums[j]==0:
#             nums[i+1],nums[j]=nums[j],nums[i+1]
#             i+=1
#     return nums




# nums = [0, 1, 0, 1, 0, 1]
# result = MoveOnesAtEnd(nums)
# print(result) 



def moveZeroes(nums: List[int]) -> None:
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0
