class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] *(n+1)

        dp[0] = 1

        for i in range(1,n+1):
            one = s[i-1]

            if one != '0':
                dp[i] += dp[i-1]
            if i >= 2:
                two = s[i-2:i]

                if 10<= int(two) <= 26:
                    dp[i] += dp[i-2]

        return dp[n] 
        