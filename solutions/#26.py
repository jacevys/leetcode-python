from typing import List
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictonary = {}

        for index, num in enumerate(nums):
            if num not in dictonary:
                dictonary[num] = -1
            else:
                nums[index] = 1000

        nums.sort()

        return len(dictonary)
#
def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    answer = solution.removeDuplicates(nums)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.09.24
(1)success
(2)time: 1 hour
(3)checked
'''
#