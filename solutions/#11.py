from typing import List
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0

        #每次移動高度較矮的那一個pointer，背後的想法是在當前最大寬度下（不管移動哪一邊，寬度都會縮減，所以當前肯定是最大寬度）
        #移動較矮的那一個pointer，寬度少一個單位下，有可能下一個高度會更高，會得到更大的面積

        while left_pointer < right_pointer:
            max_area = max(max_area, (right_pointer - left_pointer) * (min(height[left_pointer], height[right_pointer])))

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area
#
def main():
    height = [1, 8, 100, 2, 100, 4, 8, 3, 7]
    solution = Solution()
    answer = solution.maxArea(height)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.09.05
(1)failed
(2)time: 2 hours 11 minutes
(3)checked

ref:
https://www.geeksforgeeks.org/container-with-most-water/
'''
#