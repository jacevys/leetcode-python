class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        return (x == x[::-1])
#
class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        array = []

        while x >= 1:
            bit = x % 10
            array.append(bit)
            x //= 10

        return (array == array[::-1])
#
def main():
    x = -121
    solution = Solution_2()
    answer = solution.isPalindrome(x)
    print(answer)
#
if __name__ == '__main__':
    main()
#
'''
2022.08.29
(1)success
(2)time: 17 minutes
(3)checked
'''
#