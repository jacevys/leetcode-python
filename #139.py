class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:i + len(word)] == word:
                        dp[i + len(word)] = True

        return dp[-1]
'''
2023.04.17
1.failed
'''
#