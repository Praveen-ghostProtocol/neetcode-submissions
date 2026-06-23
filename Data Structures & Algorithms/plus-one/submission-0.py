class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        number = 0
        i = 0
        for j in range(n-1,-1,-1):
            number += digits[j]*(10**i)
            i += 1
        number += 1

        listr = []
        while number > 0:
            d = number % 10
            listr.append(d)
            number //= 10
        return listr[::-1]
        