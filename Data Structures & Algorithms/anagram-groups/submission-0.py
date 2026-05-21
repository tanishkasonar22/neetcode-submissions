class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for r in s:
                count[ord(r) - ord('a')] += 1

            key = tuple(count)
            ana_dict[key].append(s)

        return list(ana_dict.values())

        