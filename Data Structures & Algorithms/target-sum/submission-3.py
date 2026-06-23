class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)

        if (total+target)%2 !=0 or total+target < 0:
            return 0

        req = (total+target)//2
        dp = [[0]*(req+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(req+1):
                nottake = dp[i-1][j]
                take = 0
                if nums[i-1]<=j:
                    take = dp[i-1][j-nums[i-1]]
                dp[i][j] = take + nottake
        
        # count = 0
        return dp[n][req]
        