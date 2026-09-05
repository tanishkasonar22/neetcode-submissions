# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         counter = 0
#         maxi = 0
#         seen = []

#         for i in range(len(s)):
#             if s[i] not in seen:
#                 seen.append(s[i])
#                 counter += 1
#                 maxi = max(maxi, counter)
#             else:
#                 # Remove characters from the start of 'seen' until the duplicate is gone
#                 while s[i] in seen:
#                     seen.pop(0)
#                     counter -= 1
#                 seen.append(s[i])
#                 counter += 1
         
#         return maxi

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 # it removes all the duplicted behind till the set is completly unique. 
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res