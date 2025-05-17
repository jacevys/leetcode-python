class Solution:
    def hammingWeight(self, n: int) -> int:
        number_of_one = 0

        for i in range(32):
            number_of_one += (n % 2)
            n = n >> 1

        return number_of_one
#
def main():
    n = 0b00000000000000000000000000001011
    solution = Solution()
    answer = solution.hammingWeight(n)
    print(answer)
#
if __name__ == '__main__':
    main()
#
'''
2022.12.23
(1)success
(2)time: 15 minutes
'''