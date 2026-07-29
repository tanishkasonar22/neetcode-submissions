
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        
        # Compare each day to the previous day
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxP += prices[i] - prices[i - 1]  # Collect all profit gains
                
        return maxP
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = 0
#         r = 1
#         maxP = 0
#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(maxP, profit)

#             else:
#                 l = r
#             r += 1 #regardless of left pointer, we always have to move the right one


#         return maxP


        