from typing import List
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = int(len(nums) / 2)

        while(True):
            if target not in nums:
                return -1
            if nums[left_index] == target:
                return left_index
            if nums[right_index] == target:
                return right_index

            if nums[left_index] > target and nums[right_index] > target:
                left_index += 1
                right_index += 1
            elif nums[left_index] > target and nums[right_index] < target:
                left_index = right_index
                right_index = len(nums) - 1
            elif nums[left_index] < target:
                left_index += 1
            elif nums[right_index] > target:
                right_index -= 1
#
def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    solution = Solution()
    answer = solution.search(nums, target)
    print(answer)
#
if __name__ == '__main__':
    main()
#
'''
2022.12.23
(1)success
(2)time: 48 minutes
'''