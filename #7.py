class Solution:
    def reverse(self, x: int) -> int:
        number = 0

        sign = 1 if x > 0 else -1
        x = abs(x)

        while x >= 1:
            number *= 10
            digit = x % 10
            number += digit
            x = int(x / 10)

        if (number < (-pow(2, 31))) or (number > (pow(2, 31) - 1)):
            return 0

        return (number * sign)
#
def main():
    x = 1534236469
    solution = Solution()
    answer = solution.reverse(x)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.08.16
(1)success
(2)time: 30 minutes
(3)checked
'''
#