from typing import List
#
class Solution:
    def countBits(self, n: int) -> List[int]:
        array = []

        for i in range(n + 1):
            i_bin = bin(i).split('b')[-1]
            ones_counter = 0

            for char in i_bin:
                if char == '1':
                    ones_counter += 1

            array.append(ones_counter)

        return array
'''
2023.04.10
1.success
2.time: 15 minutes
'''
#