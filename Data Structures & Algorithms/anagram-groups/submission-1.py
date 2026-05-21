class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')]+= 1

            key = tuple(count)
            d[key].append(word)
           
            
        return list(d.values())