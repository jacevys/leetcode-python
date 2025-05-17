class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(numRows - 1):
            temp = output[i]
            row = []

            for j in range(len(temp)):
                if j == 0:
                    row.append(1)
                else:
                    row.append(temp[j] + temp[j - 1])

            row.append(1)
            output.append(row)

        return output
'''
2023.09.01
1.success
2.time: 15 minutes
'''