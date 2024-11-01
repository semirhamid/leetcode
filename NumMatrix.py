from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                self.matrix[i + 1][j + 1] = (
                    matrix[i][j] 
                    + self.matrix[i][j + 1] 
                    + self.matrix[i + 1][j] 
                    - self.matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.matrix[row2 + 1][col2 + 1] 
            - self.matrix[row1][col2 + 1] 
            - self.matrix[row2 + 1][col1] 
            + self.matrix[row1][col1]
        )
