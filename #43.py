class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dictonary = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        temp1 = 0
        temp2 = 0

        for index, digit in enumerate(num1[::-1]):
            temp1 += dictonary[digit] * pow(10, index)

        for index, digit in enumerate(num2[::-1]):
            temp2 += dictonary[digit] * pow(10, index)

        product = temp1 * temp2

        return str(product)
#
def main():
    num1 = '21321'
    num2 = '22242'
    solution = Solution()
    answer = solution.multiply(num1, num2)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.07.16: 27 minutes
2022.07.16: 檢查完成
'''
#