class Solution:
    def longestPalindrome(self, s: str) -> str:
        output_string = ''

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r + 1]) > len(output_string):
                    output_string = s[l:r + 1]

                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r + 1]) > len(output_string):
                    output_string = s[l:r + 1]

                l -= 1
                r += 1

        return output_string
'''
2023.08.22
1.success
2.time: 10 minutes
'''