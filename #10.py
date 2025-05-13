class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #initialization
        #line-5~line-7一般初始化
        m, n = len(s), len(p)
        table = [[False] * (m + 1) for i in range((n + 1))]
        table[0][0] = True

        #line-13~line-14針對p中的'*'做初始化，'*'在p中的第1個字符是沒有意義的，所以從p的第2個字符開始檢查
        #table[i][0]是指p去匹配s為空字串的情況
        #table[1][0]肯定是False，因為p的第一個字符無論是a~z、'.'、'*'都不能匹配空字串s
        #大概知道他的想法，但還沒辦法完全解釋為何可以這樣做
        for i in range(2, (n + 1)):
            table[i][0] = (table[i - 2][0]) and (p[i - 1] == '*')
#
        #line-?~line-?從上至下，從左至右更新
        #table[i][j]：當前的匹配狀態
        #table[i - 1][j - 1]：左上角的匹配狀態，指的是p[:i - 2]與s[:j - 2]是否匹配
        #p[i - 1] == s[j - 1]：指的是當前字符是否一致
        #p[i - 1] == '.'：指的是當前字符是否為萬用字元
        #所以if p[i - 1] != '*'裡的判斷式可解讀為：在p當前的字符不為'*'的情況下，當前匹配狀態 = (p[: i - 2]與s[:j - 2]為True) and ((p當前字符 == s當前字符) or (p當前字符 == '.'))
        #在p當前字符為'*'的情況下，首先要檢查p[:i - 2]或p[:i - 3]是否有True
        #還有一種情況需要考慮，上面兩格均為False的情況下，p中前一個字符p[i - 2]與s中當前字符s[j - 1]相等或是p[i - 2]是'.'，
        #則當前匹配狀態table[i][j] |= table[i][j - 1]
        for i in range(1, (n + 1)): #p
            for j in range(1, (m + 1)): #s
                if p[i - 1] != '*':
                    table[i][j] = (table[i - 1][j - 1]) and ((p[i - 1] == s[j - 1]) or (p[i - 1] == '.'))#
                else:
                    table[i][j] = (table[i - 2][j]) or (table[i - 1][j])

                    if (p[i - 2] == s[j - 1]) or (p[i - 2] == '.'):
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]
#
def main():
    s = 'abbba'
    p = 'ab*a'
    solution = Solution()
    answer = solution.isMatch(s, p)
    print(answer)
#
if __name__ == '__main__':
    main()
'''
2022.08.28
(1)failed
(2)time: 6 hours
(3)checked

ref:
https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
https://www.cnblogs.com/ltb6w/p/14747212.html
'''
#