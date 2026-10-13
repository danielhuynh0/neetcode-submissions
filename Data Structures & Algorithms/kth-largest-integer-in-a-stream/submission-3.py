class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    # heapq.heapreplace replaces the minimum val in the heap with the replacement val and heapifies
    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            if val <= self.heap[0]:
                return self.heap[0]
            heapq.heapreplace(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]

    


