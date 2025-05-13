from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        hash_table = {}
#
        for index, num in enumerate(nums):
            if index == 0:
                hash_table[index + 1] = num
            elif index == 1:
                hash_table[index + 1] = max(num, hash_table[index])
            else:
                trial_1 = num + hash_table[index - 1]
                trial_2 = hash_table[index]
                hash_table[index + 1] = max(trial_1, trial_2)

        return max(hash_table.values())
#
    def rob_2(self, nums: List[int]) -> int:
        hash_table = {}

        return self.function_1(0, nums, hash_table)
#
    def function_1(self, i, nums, hash_table):
        if i >= len(nums):
            return 0

        if i in hash_table:
            return hash_table[i]

        maximum = max(self.function_1(i + 1, nums, hash_table), self.function_1(i + 2, nums, hash_table) + nums[i])
        hash_table[i] = maximum

        return maximum
#
def main():
    nums = [2, 1, 1, 2]
    solution = Solution()
    answer = solution.rob(nums)
    print(answer)
#
if __name__ == '__main__':
    main()
#
'''
2022.11.19
(1)sucess
(2)1.5 hour
(3)checked
'''
#