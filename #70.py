class Solution:
    def climbStairs(self, n: int) -> int:
        dictionary = {0: 0, 1: 1, 2: 2}

        self.function(dictionary, n)

        return dictionary[n]
#
    def function(self, dictionary, n):
        if n not in dictionary:
            dictionary[n] = self.function(dictionary, n - 1) + self.function(dictionary, n - 2)
            return dictionary[n]
        else:
            return dictionary[n]
#2023.03.09
class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {0: 0, 1: 1, 2: 2}

        self.function(n, dict)

        return dict[n]

    def function(self, n, dict):
        if n in dict:
            return dict[n]
        else:
            dict[n] = self.function(n - 1, dict) + self.function(n - 2, dict)
            return dict[n]
#2023.08.23
'''
2023.03.09
1.success
2.time: 31 mins
2023.08.23
1.failed
2.time: 1 hour
'''