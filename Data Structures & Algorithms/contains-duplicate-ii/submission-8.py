class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()
        
        for i in range(len(nums)):
            # 1. Did we see this number recently?
            if nums[i] in seen:
                return True
            
            # 2. Store current number
            seen.add(nums[i])
            
            # 3. If the window gets too big, remove the oldest number
            if len(seen) > k:
                seen.remove(nums[i - k])
                
        return False