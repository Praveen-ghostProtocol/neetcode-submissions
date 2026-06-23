class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        maxint = 0x7fffffff

        while b!=0:
            carry = (a&b) << 1
            a = (a^b) & mask
            b = carry & mask

        if a<=maxint:
            return a
        else:
            return ~(a ^ mask)