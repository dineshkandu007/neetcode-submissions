class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy pointer
        left = 0

        # Sell pointer
        right = 1

        # Maximum profit found
        max_profit = 0

        # Move sell pointer through the array
        while right < len(prices):

            # If selling price is greater than buying price
            if prices[right] > prices[left]:

                # Calculate current profit
                profit = prices[right] - prices[left]

                # Keep the maximum profit
                max_profit = max(max_profit, profit)

            else:
                # Found a cheaper buying price
                left = right

            # Move sell day forward
            right += 1

        return max_profit