class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def helper(n):
            squaresum = 0
            while n > 0:
                d = n%10
                squaresum += d**2
                n = n//10
            return squaresum
        
        while n not in seen:
            if n == 1:
                return True
            
            seen.add(n)
            n = helper(n)
        return False

