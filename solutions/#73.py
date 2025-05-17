class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_index = []
        column_index = []
        m, n = len(matrix), len(matrix[0])

        for index, row in enumerate(matrix):
            if 0 in row:
                row_index.append(index)

            for index_2, column_element in enumerate(row):
                if column_element == 0:
                    column_index.append(index_2)

        for index in row_index:
            for index_2 in range(n):
                matrix[index][index_2] = 0

        for index in column_index:
            for index_2 in range(m):
                matrix[index_2][index] = 0
'''
2023.07.18
1.failed
'''