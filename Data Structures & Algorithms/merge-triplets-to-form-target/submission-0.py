class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundx = False
        foundy = False
        foundz = False

        for a,b,c in triplets:
            if a > target[0] or b > target[1] or c>target[2]:
                continue
            
            if a == target[0]:
                foundx = True
            if b == target[1]:
                foundy = True
            if c == target[2]:
                foundz = True
            
        return foundx and foundy and foundz