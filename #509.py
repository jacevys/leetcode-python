class Solution:
    def fib(self, n: int) -> int:
        f_1, f_2 = 0, 1
        f_n = 0

        if n == 0 or n == 1:
            return n

        for i in range(n - 1):
            f_n = f_1 + f_2
            f_1, f_2 = f_2, f_n

        return f_2
'''
2023.08.30
1.success
2.time: 10 minutes
'''