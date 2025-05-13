from typing import List
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictonary = {}

        for index, num in enumerate(nums):
            difference = target - num

            if num in dictonary.keys():
                return [dictonary[num], index]
            else:
                dictonary[difference] = index
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, num in enumerate(nums):
            if num not in dict:
                dict[target - num] = index
            else:
                return [index, dict[num]]
#
def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.07.01: 45 minutes
2022.07.11: 檢查完成
2022.09.25: review｜可不用再看
2023.08.23: 6 minutes
2023.08.23: 可不用複習
'''
#