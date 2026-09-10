class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i = 0
        res = 0
        min_len = float('inf') #infinite 

        for j in range(len(nums)):

            res += nums[j]

            while res >= target:
                min_len = min(min_len, j - i + 1)
                res -= nums[i]
                i += 1

        if min_len == float('inf'):
            return 0

        return min_len