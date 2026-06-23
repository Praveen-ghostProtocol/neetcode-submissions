class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])

        result = []
        visited = set()

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        direction = 0
        row, col = 0,0

        for _ in range(m*n):
            result.append(matrix[row][col])
            visited.add((row,col))

            dr,dc = directions[direction]
            nextrow, nextcol = row + dr, col + dc

            if nextrow < 0 or nextrow >=m or nextcol <0 or nextcol >=n or (nextrow,nextcol) in visited:
                direction = (direction+1)%4
                dr,dc = directions[direction]
                nextrow, nextcol = row + dr, col + dc

            row, col = nextrow, nextcol
        return result