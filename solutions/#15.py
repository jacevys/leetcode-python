from typing import List
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = set()

        for index, value in enumerate(nums):
            if (index >= 1) and (value == nums[index - 1]):
                continue

            dictonary = {}

            for num in nums[index + 1:]:
                if num not in dictonary:
                    dictonary[-value-num] = 1
                else:
                    result.add((value, -value-num, num))

        return result
#
def main():
    nums = [1, -1, 0, 2, 3]
    solution = Solution()
    answer = solution.threeSum(nums)
#
if __name__ == '__main__':
    main()
'''
2022.09.16
(1)failed
(2)time: 3 hours
(3)checked

ref:
https://ithelp.ithome.com.tw/articles/10213264
'''
#