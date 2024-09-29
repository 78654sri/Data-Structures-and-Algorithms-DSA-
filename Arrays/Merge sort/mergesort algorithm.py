# def merge_sort(nums, startindex, endindex):
#     if startindex < endindex:
#         mid = (startindex + endindex) // 2
#         merge_sort(nums, startindex, mid)
#         merge_sort(nums, mid + 1, endindex)
#         merge(nums, startindex, mid, endindex)
# def merge(nums, startindex, mid, endindex):
#     left = nums[startindex:mid + 1]
#     right = nums[mid + 1:endindex + 1]
#     leftIndex = 0
#     rightIndex = 0
#     sortedIndex = startindex

#     while leftIndex < len(left) and rightIndex < len(right):
#         if left[leftIndex] <= right[rightIndex]:
#             nums[sortedIndex] = left[leftIndex]
#             leftIndex += 1
#         else:
#             nums[sortedIndex] = right[rightIndex]
#             rightIndex += 1
#         sortedIndex += 1

#     while leftIndex < len(left):
#         nums[sortedIndex] = left[leftIndex]
#         leftIndex += 1
#         sortedIndex += 1

#     while rightIndex < len(right):
#         nums[sortedIndex] = right[rightIndex]
#         rightIndex += 1
#         sortedIndex += 1
# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums, 0, len(nums) - 1)
# print(nums)
