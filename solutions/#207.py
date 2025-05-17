class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i: [] for i in range(numCourses)}
        indegrees = [0 for i in range(numCourses)]

        for i, j in prerequisites:
            edges[j].append(i)
            indegrees[i] += 1

        queue, count = deque([]), 0

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count += 1

            for x in edges[node]:
                indegrees[x] -= 1

                if indegrees[x] == 0:
                    queue.append(x)

        return count == numCourses
'''
2023.05.01
1.failed
'''