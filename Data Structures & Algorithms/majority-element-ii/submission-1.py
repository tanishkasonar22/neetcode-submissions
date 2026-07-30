from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()          
        n = len(nums)
        i = 0
        j = n // 3 # its constant number 
        seen = set()
        
        for i in range(n - j):
            if nums[i] == nums[i + j]: #constant tie to i
                seen.add(nums[i])   

        return list(seen)