class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n+1)]
        def solve(coins,n,amount):
            if amount == 0:
                return 0
            if n == 0:
                return float('inf')
            if dp[n][amount] != -1:
                return dp[n][amount]
            nottake = solve(coins,n-1,amount)

            take = float('inf')
            if coins[n-1] <= amount:
                take = 1+ solve(coins, n, amount-coins[n-1])
            
            dp[n][amount] = min(take,nottake)
            return dp[n][amount]
        
        ans = solve(coins,n,amount)
        return ans if ans != float('inf') else -1
