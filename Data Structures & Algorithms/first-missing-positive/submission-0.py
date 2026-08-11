class Solution:

    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct index position (nums[i] should be i + 1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Step 2: Find the first index where the number doesn't match i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all numbers 1..n are present, the answer is n + 1
        return n + 1