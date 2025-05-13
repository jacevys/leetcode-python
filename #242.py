class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stack = []

        for char in s:
            stack.append(char)

        for char in t:
            if char in stack:
                stack.remove(char)
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False

'''
2023.03.08
1.success
2.time: 33 minutes
'''