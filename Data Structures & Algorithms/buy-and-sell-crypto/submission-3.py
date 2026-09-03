class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # i = min(prices)
        # j = len(prices)-1
        # res = []
        # while i < j:
        #     if prices[j-1] >= prices[j]:
        #         res.append(prices[j-1])
        #         j -= 1
        #     else:
        #         res.append(prices[j])
        #         j -= 1
            
        # return max(res) - prices[i]
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest buying price seen so far
            if price < min_price:
                min_price = price
            # Check profit if we sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

        

        