class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}

        if len(strs) < 1:
            return strs
        else:
            for i in range(len(strs)):
                reg = strs[i]
                regsort = ''.join(sorted(reg))

                if regsort in solution:
                    solution[regsort].append(reg)
                else:
                    solution[regsort] = [reg]

        return solution.values()
'''
2023.07.31
1.failed
'''