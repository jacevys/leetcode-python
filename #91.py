class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                continue

            dp[i] += dp[i + 1]

            if len(s[i:]) >= 2:
                if int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]
'''
2023.04.22
1.failed
'''
#