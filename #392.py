class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(t)):
            if s == '':
                return True
            if t[i] == s[0]:
                s = s[1:]

        return s == ''
'''
2023.09.11
1.success
2.time: 5 minutes
'''