from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])

        i = 0

        while i < len(intervals):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]

            if result:
                prev_start, prev_end = result[-1]
                hi = min(prev_end, cur_end)
                lo = max(prev_start, cur_start)

                if lo <= hi:
                    if cur_end > prev_end:
                        result[-1][1] = cur_end
                else:
                    result.append(intervals[i])
            else:
                result.append(intervals[i])

            i += 1

        return result
'''
2023.07.10
1.failed
'''