class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        count = [0, 0, 0]

        for i in range(len(nums)):
            if nums[i] == 0:
                count[0] += 1
            elif nums[i] == 1:
                count[1] += 1
            else:
                count[2] += 1

        j = 0

        for i, c in enumerate(count):
            while c != 0:
                if i == 0:
                    nums[j] = 0
                elif i == 1:
                    nums[j] = 1
                else:
                    nums[j] = 2
                c -= 1
                j += 1
        '''
        p, q = 0, 0
        k = len(nums) - 1

        while q <= k:
            if p < q and nums[q] == 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            elif nums[q] == 2:
                nums[q], nums[k] = nums[k], nums[q]
                k -= 1
            else:
                q += 1
'''
2023.09.11
1.success
2.time: 15 minutes
'''