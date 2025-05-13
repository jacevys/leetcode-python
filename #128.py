class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in hash_set:
                curr = num
                curr_len = 1

                while (curr + 1) in hash_set:
                    curr_len += 1
                    curr += 1

                res = max(res, curr_len)

        return res
'''
2023.05.08
1.failed
'''
#