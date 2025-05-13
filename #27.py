class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        k = 0
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
            else:
                k += 1

        nums.sort()

        return k
        '''
        i, last = 0, len(nums) - 1

        while i <= last:
            if nums[i] == val:
                nums[i] , nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1

        return last + 1
'''
2023.09.06
1.success
2.time: 23 minutes
'''