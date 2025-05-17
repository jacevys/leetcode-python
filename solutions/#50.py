class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1

        if x == 1:
            return 1
        elif x == -1:
            if n < 0:
                return 1

            return (-1) * (n % 2)

        for power in range(abs(n)):
            if n >= 0:
                result *= x
            else:
                result /= x

            if result > 10e4:
                return 10e4
            elif result < -(10e4):
                return -(10e4)
            elif result == 0:
                return 0

        return result
#
def main():
    x = -1
    n = -2147483648
    solution = Solution()
    answer = solution.myPow(x, n)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.07.13: 1 hour 9 minutes
2022.07.13: 檢查完成
*待參考別人的演算法
'''