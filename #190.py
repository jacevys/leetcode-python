class Solution:
    def reverseBits(self, n: int) -> int:
        n_str = str(bin(n).split('b')[1])

        while len(n_str) < 32:
            n_str = '0' + n_str

        n_reverse = int(n_str[::-1], 2)

        return n_reverse
'''
2023.04.15
1.success
2.time: 35 minutes
'''
#