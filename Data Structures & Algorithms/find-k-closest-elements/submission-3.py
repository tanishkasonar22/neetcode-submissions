class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - 1
        while hi - lo >= k:
            if abs(x - arr[lo]) > abs(x - arr[hi]):
                lo += 1
            else:
                hi -= 1
        return arr[lo:hi + 1]


        ## paractice this logic