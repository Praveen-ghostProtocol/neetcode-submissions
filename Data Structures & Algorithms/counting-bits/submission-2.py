class Solution:
    def countBits(self, n: int) -> List[int]:
        # result = [0] * (n+1)

        # for i in range(1,n+1):
        #     result[i] = result[i>>1] + (i&1)
        # return result

        def counter(num):
            count = 0
            while num > 0:
                count += num&1
                num>>=1
            return count
        
        result= []
        for i in range(n+1):
            result.append(counter(i))
        return result