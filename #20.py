class Solution:
    def isValid(self, s: str) -> bool:
        dictonary = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            stacked_char = ''

            if char in dictonary.values():
                stack.append(char)
            else:
                if len(stack) > 0:
                    stacked_char = stack.pop()

                if dictonary[char] != stacked_char:
                    return False

        return (len(stack) == 0)
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                bracket = stack.pop()

                if char == ')' and bracket != '(':
                    return False
                if char == ']' and bracket != '[':
                    return False
                if char == '}' and bracket != '{':
                    return False

        return len(stack) == 0
#
def main():
    s = '()))'
    solution = Solution()
    answer = solution.isValid(s)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.09.07
(1)success
(2)time: 35 minutes
(3)checked

2023.08.22
1.success
2.time: 10 minutes
'''
#