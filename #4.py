from typing import List
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for nums in nums2:
            nums1.append(nums)

        nums1.sort()

        if (len(nums1) % 2) == 0:
            median = (nums1[int(len(nums1) / 2) - 1] + nums1[int(len(nums1) / 2)]) / 2
        else:
            median = nums1[int(len(nums1) / 2)]

        return median
#
def main():
    nums1 = [1, 2]
    nums2 = [3, 4, 0]
    solution = Solution()
    answer = solution.findMedianSortedArrays(nums1, nums2)
#
if __name__ == '__main__':
    main()
'''
2022.08.14
(1)success
(2)time: 28 minutes
(3)chenked

2022.09.25
(1)review｜不用再看
'''
#