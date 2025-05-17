from typing import List
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
#
'''
2023.03.09
1.success
2.time: 50 mins
'''