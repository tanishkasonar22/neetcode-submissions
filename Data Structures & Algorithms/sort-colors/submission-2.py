# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] > nums[j]:
#                     nums[i], nums[j] = nums[j], nums[i]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        mid = 0
        right = len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        