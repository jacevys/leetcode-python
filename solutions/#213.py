class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_iterative(nums[:-1]), self.rob_iterative(nums[1:]))

    def rob_iterative(self, nums):
        one_step = 0
        two_step = 0

        for num in nums:
            temp = one_step
            one_step = max(one_step, two_step + num)
            two_step = temp

        return one_step
#
'''
2023.04.17
1.failed
'''
#