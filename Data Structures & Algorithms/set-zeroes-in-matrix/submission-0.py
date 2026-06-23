class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        firstrowzero = False
        firstcolzero = False

        for c in range(cols):
            if matrix[0][c] == 0:
                firstrowzero = True
                break
        for r in range(rows):
            if matrix[r][0] == 0:
                firstcolzero = True
                break
        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, rows):
            for c in range(1,cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if firstrowzero:
            for c in range(cols):
                matrix[0][c] = 0
        
        if firstcolzero:
            for r in range(rows):
                matrix[r][0] = 0

        
        