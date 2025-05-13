from typing import List
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.insert(-1, target)

        nums.sort()
        index = nums.index(target)

        return index
#
def main():
    nums = [1, 3, 5, 6]
    target = 2
    solution = Solution()
    answer = solution.searchInsert(nums, target)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.07.02: 22 minutes
2022.07.11: 檢查完成
'''
#