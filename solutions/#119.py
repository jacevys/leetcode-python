class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            temp = list(row)

            for j in range(1, i + 1):
                row[j] = temp[j] + temp[j - 1]

        return row
'''
2023.09.11
1.success
2.time: 42 minutes
'''