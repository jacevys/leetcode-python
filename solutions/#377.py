class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for total in range(1, target + 1):
            dp[total] = 0

            for num in nums:
                dp[total] += dp.get(total - num, 0)

        return dp[target]
#
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]
#
'''
2023.04.17
1.failed
'''
#