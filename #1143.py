class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dp_grid[row][col] = dp_grid[row + 1][col + 1] + 1
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

        return dp_grid[0][0]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        #current: current column
        #previous: previous column
        current = [0] * (len(text1) + 1)
        previous = [0] * (len(text1) + 1)

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = previous[row + 1] + 1
                else:
                    current[row] = max(previous[row], current[row + 1])

            current, previous = previous, current

        return previous[0]
'''
2023.04.15
1.failed
'''
#