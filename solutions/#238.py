from typing import List
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = 1
        array = [1] * len(nums)

        for i in range(1, len(nums)):
            array[i] = array[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            array[i] *= right_product
            right_product = right_product * nums[i]

        return array
#2022.12.22
'''
nums = [1, 2, 3, 4]
array = [1, 1x1, 1x1x2, 1x1x2x3] = [1, 1, 2, 6] #不包含i-th元素的左乘積

i = 3, array[3] *= 1 = 6, rp = 1 * nums[3] = 4
i = 2, array[2] *= 4 = 8, rp = 4 * nums[2] = 4 * 3
i = 1, array[1] *= 12 = 12, rp = 12 * nums[1] = 4 * 3 * 2
i = 0, array[0] *= 24 = 24, rp = 24 * nums[0] = 24
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = 1

        for i in range(len(nums)):
            result *= nums[i]
            prefix.append(result)

        result = 1

        for i in range(len(nums) - 1, -1, -1):
            result *= nums[i]
            postfix.append(result)

        postfix.reverse()

        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]

        return nums
#2023.08.23
def main():
    nums = [1, 2, 3, 4, 5]
    solution = Solution()
    answer = solution.productExceptSelf(nums=nums)
#
if __name__ == '__main__':
    main()
#
'''
2022.12.22
(1)failed
(2)time: 1 hour 12 minutes
2023.08.23
1.failed
2.time: 1 hour
'''