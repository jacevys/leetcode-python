class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)
        '''
        k = k % len(nums)

        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]
'''
2023.10.09
1.success
2.time: 8 minutes
'''