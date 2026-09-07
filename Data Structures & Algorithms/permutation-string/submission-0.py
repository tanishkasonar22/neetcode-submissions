class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        seen = []
        res = []
        
        # Sort s1 so order won't matter when comparing
        for i in range(len(s1)):
            seen.append(s1[i])
        seen.sort()

        for r in range(len(s2)):
            # 1. Always append the new character to your window
            res.append(s2[r])

            # 2. Once window exceeds length of s1, drop the leftmost character
            if len(res) > len(s1):
                res.pop(0)
                l += 1

            # 3. Check if the sorted window matches sorted s1
            if len(res) == len(s1) and sorted(res) == seen:
                return True

        return False