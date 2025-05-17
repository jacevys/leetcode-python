from typing import List
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        pointer_1 = 0
        pointer_2 = 0

        while(True):
            if pointer_1 >= len(prices) or pointer_2 >= len(prices):
                break

            difference = prices[pointer_2] - prices[pointer_1]

            if difference < 0:
                pointer_1 += 1
            else:
                max_profit = max(max_profit, difference)
                pointer_2 += 1

        return max_profit
#
def main():
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    answer = solution.maxProfit(prices=prices)
#
if __name__ == '__main__':
    main()
#
'''
2022.12.22
(1)success
(2)time: 50 minutes
'''