class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            dist_sq = (x*x) + (y*y)
            heapq.heappush(heap, (dist_sq, point))

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans