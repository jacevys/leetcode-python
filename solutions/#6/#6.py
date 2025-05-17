class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = [[] for i in range(numRows)]
        x_index = 0
        direction_flag = False
        output_string = ''

        if numRows == 1:
            return s

        for char in s:
            if direction_flag == False: #down
                array[x_index].append(char)
                x_index += 1

                if x_index == (numRows):
                    x_index -= 1
                    direction_flag = True
            else: #up
                x_index -= 1
                array[x_index].append(char)
                if x_index == 0:
                    x_index += 1
                    direction_flag = False

        for string in array:
            for char in string:
                output_string += char

        return output_string
#
def main():
    s = 'PAYPALISHIRING'
    numRows = 4
    solution = Solution()
    answer = solution.convert(s, numRows)
#
if __name__ == '__main__':
    main()
'''
2022.09.15
(1)success
(2)time: 1 hour 24 minutes
(3)
'''
#