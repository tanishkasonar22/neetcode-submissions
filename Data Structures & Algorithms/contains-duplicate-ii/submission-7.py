class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
            
        i = 0
        j = 1
        while j < len(nums):
            while abs(i - j) <= k and j < len(nums):
                if nums[i] == nums[j]:
                    return True
                j += 1
            i += 1
            j = i + 1
            
        return False