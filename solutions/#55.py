class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_index = 0
        last_index = len(nums) - 1

        for i in range(len(nums)):
            if i > end_index:
                return False
            if nums[i] + i > end_index:
                end_index = nums[i] + i
            if end_index >= last_index:
                return True
'''
2023.04.22
1.failed
'''
#