class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_val = 0
        
        while i < j:
            l = min(heights[i], heights[j])
            b = j - i
            res = l * b
            
            if res > max_val:
                max_val = res
                
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_val