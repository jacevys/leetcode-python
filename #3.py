class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for start_index in range(len(s)):
            substring = ''
            substring += s[start_index]

            for end_index in range((start_index + 1), len(s)):
                if s[end_index] not in substring:
                    substring += s[end_index]
                else:
                    break

            if len(substring) > max_length:
                max_length = len(substring)

        return max_length
#
class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_index = 0
        max_length = 0
        usedChar = {}

        for end_index in range(len(s)):
            if (s[end_index] in usedChar) and (start_index <= usedChar[s[end_index]]):
                start_index = usedChar[s[end_index]] + 1
            else:
                max_length = max(max_length, end_index - start_index + 1)

            usedChar[s[end_index]] = end_index

        return max_length
#
def main():
    s = 'bbbbb'
    solution = Solution()
    answer = solution.lengthOfLongestSubstring(s)
    print(answer)

    s_2 = 'pwwekww'
    solution_2 = Solution_2()
    answer_2 = solution_2.lengthOfLongestSubstring(s_2)
    print(answer_2)
#
if __name__ == '__main__':
    main()
'''
2022.08.11
(1)success
(2)time: 34 minutes
(3)checked

2022.09.25
(1)review

ref:
https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
'''
#