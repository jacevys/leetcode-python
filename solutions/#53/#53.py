from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] > 0: #當前為第i個位置，如果第（i - 1）個位置前的最大值小於0，那麼就沒必要加了，直接忽略
                nums[i] = nums[i - 1] + nums[i] #包含第i個位置的值的情況下的最大值

            result = max(result, nums[i]) #index為i時的最大值，可包含i也可不包含i

        return result
#