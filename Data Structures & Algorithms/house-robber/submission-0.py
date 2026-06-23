class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        def solve(i):
            if i<0:
                return 0
            if i == 0:
                return nums[0]
            if dp[i] != -1:
                return dp[i]

            take = nums[i] + solve(i-2)
            notake = solve(i-1)

            dp[i] = max(take,notake)
            return dp[i]
        return solve(n-1)
        