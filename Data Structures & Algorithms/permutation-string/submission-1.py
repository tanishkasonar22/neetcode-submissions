from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_count = Counter(s1)
        
        # Check every substring of length k in s2
        for i in range(len(s2) - k + 1):
            if Counter(s2[i : i + k]) == s1_count:
                return True
                
        return False