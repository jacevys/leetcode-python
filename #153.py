from typing import List
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_index = 0
        right_index = int(len(nums) / 2)
        minimum = 0

        while(True):
            if (left_index == right_index) or (right_index >= len(nums)):
                minimum = nums[left_index]
                break

            if nums[left_index] < nums[right_index]:
                right_index += 1
            else:
                left_index += 1

        return minimum
#
def main():
    nums = [11, 13, 15, 17]
    solution = Solution()
    answer = solution.findMin(nums)
#
if __name__ == '__main__':
    main()
#
'''
2022.12.22
(1)success
(2)time: 30 minutes
'''