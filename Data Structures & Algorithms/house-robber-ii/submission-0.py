class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        def rob_linear(arr):
            k = len(arr)
            dp = [0] * (n+1)

            dp[0] = 0
            if k>=1:
                dp[1] = arr[0]
            for i in range(2,k+1):
                notrob = dp[i-1]
                rob = arr[i-1] + dp[i-2]

                dp[i] = max(rob,notrob)
            return dp[k]
        
        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])
        return max(case1,case2)