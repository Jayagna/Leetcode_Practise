class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1

        coins.sort() 

        if coins[0] > amount:
            return -1
        
        dp = [-1]*(amount+1)
        dp[0] = 0

        smallest = coins[0]
        for i in range(1,smallest):
            dp[i] = -1

        for j in range(smallest,amount+1):
            minimum = float("inf")
            if j in coins:
                dp[j] = 1
            for i in range(len(coins)):
                if j - coins[i] >= 0 and dp[j - coins[i]] != -1:
                    minimum = min(minimum,dp[j-coins[i]])
            if minimum != float("inf"):
                dp[j] = minimum + 1

        return dp[-1]