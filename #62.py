class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_step = (m - 1) + (n - 1)

        temp_1 = 1
        temp_2 = 1
        temp_3 = 1

        for i in range(total_step):
            temp_1 *= (i + 1)

        for i in range(m - 1):
            temp_2 *= (i + 1)

        for i in range(n - 1):
            temp_3 *= (i + 1)

        total_count = temp_1 / (temp_2 * temp_3)

        return int(total_count)
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m_real, n_real = m - 1, n - 1
        hash_map = {}

        return self.function(m_real, n_real, hash_map)

    def function(self, m, n, hash_map):
        if m == 0 or n == 0:
            return 1

        if (m, n) in hash_map:
            return hash_map[(m, n)]
        else:
            hash_map[(m, n)] = self.function(m - 1, n, hash_map) + self.function(m, n - 1, hash_map)

        return hash_map[(m, n)]
#
'''
2023.04.22
1.success
2.time: 15 minutes
'''
#