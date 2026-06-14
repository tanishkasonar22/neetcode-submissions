class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #logic: substring is to maintain the window. From the i = 0 till max it have the same letter.

        res = "" # create the empty set to store the prefix
        for i in range(len(strs[0])):  # for i in rangle (0,1,2,3,4,5)
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            res += strs[0][i]
        return res