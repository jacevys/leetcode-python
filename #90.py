class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subsets.append([])
        start_idx = 0
        end_idx = 0

        for i in range(len(nums)):
            start_idx = 0

            if i > 0 and nums[i] == nums[i - 1]:
                start_idx = end_idx + 1

            end_idx = len(subsets) - 1

            for j in range(start_idx, end_idx + 1):
                copy_set = list(subsets[j])
                copy_set.append(nums[i])
                subsets.append(copy_set)

        return subsets
'''
2023.10.10
1.failed
'''