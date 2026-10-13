class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1*stone for stone in stones]
        heapq.heapify(heap)

        # can use heapify_max(), heappop_max() and heappush_max()
        while len(heap) > 1:
            first = -1*heapq.heappop(heap)
            second = -1*heapq.heappop(heap)

            if first == second:
                continue
            winner = max(first, second) - min(first, second)
            heapq.heappush(heap, -1*winner)
        
        return -1*heap[0] if heap else 0

