class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)

        dp[0] = 0
        if n>=1:
            dp[1] = nums[0]
        for i in range(2,n+1):
            notrob = dp[i-1]
            rob = nums[i-1] + dp[i-2]

            dp[i] = max(rob,notrob)
        return dp[n]