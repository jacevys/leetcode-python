from typing import List
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        number_of_layer = int(len(matrix) / 2)

        for layer_index in range(number_of_layer):
            first_position = layer_index
            last_position = length - layer_index - 1

            for element in range(first_position, last_position):
                offset = element - first_position

                top = matrix[first_position][element]
                right = matrix[element][last_position]
                bottom = matrix[last_position][last_position - offset]
                left = matrix[last_position - offset][first_position]

                matrix[first_position][element] = left
                matrix[element][last_position] = top
                matrix[last_position][last_position - offset] = right
                matrix[last_position - offset][first_position] = bottom
#
def main():
    matrix = [[i for i in range(j * 5, (j + 1) * 5)] for j in range(5)]
    print('original matrix:')
    printMatrix(matrix)
    solution = Solution()
    answer = solution.rotate(matrix)
    print('rotated matrix:')
    printMatrix(answer)
#
def printMatrix(matrix):
    for row in matrix:
        print(row)
#
if __name__ == '__main__':
    main()
'''
2022.08.09
(1)failed
(2)45 minutes + 56 minutes + 1 hour 2 minutes
(3)檢查完成

ref:
https://tw.coderbridge.com/questions/28dff788e22845319539c29c02dca96e
'''
#