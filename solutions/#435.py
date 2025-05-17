from typing import List
#
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        previous = None
        counter = 0

        for interval in intervals:
            if previous == None:
                previous = interval
                continue

            if interval[0] < previous[1]:
                counter += 1
                continue

            previous = interval

        return counter
#
def main():
    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    solution = Solution()
    answer = solution.eraseOverlapIntervals(intervals)
    print(answer)
#
if __name__ == '__main__':
    main()
#
'''
2023.07.12
1.success
2.time: 15 minutes
'''
#