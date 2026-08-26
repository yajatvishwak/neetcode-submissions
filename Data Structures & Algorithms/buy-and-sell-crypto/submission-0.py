class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = 0
        max_price = 0
        for i in range(len(prices)-1, -1, -1):
            price = prices[i]
            max_so_far = max(max_so_far, price)
            max_price  = max(max_price, max_so_far - price)
        return max_price
        
        