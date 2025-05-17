class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        remain = 0

        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]

        return start
'''
2023.09.18
1.failed
2.time: 20 minutes
'''