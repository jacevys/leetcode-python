class Solution:
    def isPalindrome(self, s: str) -> bool:
        #solution 1
        '''
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
        '''

        #solution 2
        s_2 = ''

        for char in s:
            if char.isalnum():
                s_2 += char.lower()

        return s_2[::] == s_2[::-1]
'''
2023.08.22
1.failed
'''