class Solution:
    def myAtoi(self, s: str) -> int:
        integer = 0
        sign = 1
        signed = False
        dictonary = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                     '-': -1, '+': 1}
#
        for char in s:
            if (char == ' ') and (signed == False):
                continue
            elif (char == '-' or char == '+'):
                if signed == True:
                    break
                sign *= dictonary[char]
                signed = True
                continue
            elif char not in dictonary.keys():
                break
#
            digit = dictonary[char]
            integer = integer * 10 + digit
            signed = True

        integer *= sign
        integer = min(pow(2, 31) - 1, integer)
        integer = max(-pow(2, 31), integer)

        return integer
#
def main():
    s = '   + 0 123'
    solution = Solution()
    answer = solution.myAtoi(s)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.09.06
(1)sucess
(2)time: 1 hour 1 minute
(3)checked
'''
#