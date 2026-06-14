class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i,nums in enumerate(nums):
            diff = target - nums

            if diff in d:
                return [d[diff], i]

            d[nums] = i
        