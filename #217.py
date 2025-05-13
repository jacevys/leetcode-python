from typing import List
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set(nums)
        return True if len(nums) != len(set_of_nums) else False
#
'''
2023.03.30
1.success
2.time: 19 minutes
'''