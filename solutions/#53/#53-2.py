class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] = nums[i - 1] + nums[i]

            maxSum = max(maxSum, nums[i])

        return maxSum
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])

        return max(nums)
#
'''
nums[i]: 包含nums[i]的當前最大值
思路：當前位置為i, 如果nums[i - 1] < 0,
則表示0 ~ i - 1位置的最大子串列和為負數,
所以只考慮nums[i - 1]為正數的情況去看是否大於當前最大的和

2023.08.13
1.success
2023.08.23
1.success
2.time: 10 minutes
'''