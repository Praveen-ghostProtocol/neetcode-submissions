class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(nums)

        memo = [[-1] * (n+2) for _ in range(n+2)]

        def dp(i,j):
            if i>j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            ans = -math.inf
            for k in range(i,j+1):
                left = dp(i,k-1)
                right = dp(k+1,j)

                coins = arr[i-1] * arr[k] * arr[j+1]
                total = left + coins + right
                ans = max(ans, total)
            memo[i][j] = ans
            return ans
        return dp(1,n)