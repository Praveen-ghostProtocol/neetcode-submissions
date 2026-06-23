class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        maxdp = [0] * n
        mindp = [0] * n

        maxdp[0] = nums[0]
        mindp[0] = nums[0]

        ans = nums[0]

        for i in range(1,n):
            current = nums[i]

            option1 = current
            option2 = current * maxdp[i-1]
            option3 = current * mindp[i-1]
            
            maxdp[i] = max(option1,option2,option3)
            mindp[i] = min(option1,option2,option3)

            ans = max(ans, maxdp[i])
        return ans
        