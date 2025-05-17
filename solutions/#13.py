class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500,
                      'M': 1000}

        integer = 0
        previous = ''
#
        for char in s:
            integer += dictionary[char]

            if previous == '':
                pass
            elif dictionary[previous] < dictionary[char]:
                integer -= dictionary[previous] * 2

            previous = char

        return integer
#
def main():
    s = 'MCMXCIV'
    solution = Solution()
    answer = solution.romanToInt(s)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.08.31
(1)success
(2)time: 40 minutes
(3)checked
'''
#