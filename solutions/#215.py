class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
'''
date / time cost
2025.05.14, 15 m 31 s
'''