class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0]*(amount+1) for _ in range(n+1)]

        for j in range(amount+1):
            dp[0][j] = 0
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1,n+1):
            for j in range(0,amount + 1):
                nottake = dp[i-1][j]

                take = 0
                if coins[i-1] <= j:
                    take = dp[i][j-coins[i-1]]
                
                dp[i][j] = take + nottake
        return dp[n][amount]
        