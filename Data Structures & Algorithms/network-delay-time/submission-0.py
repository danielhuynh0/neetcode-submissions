class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for time in times:
            ui, vi, ti = time
            adj[ui].append(time)

        pq = []
        finished = set()
        ans = -1

        pq.append((0, k))
        while pq:
            path_weight, node = heapq.heappop(pq)
            if node in finished:
                continue
            
            finished.add(node)
            ans = path_weight if path_weight > ans else ans

            for edge in adj[node]:
                if edge[1] not in finished:
                    heapq.heappush(pq, (path_weight + edge[2], edge[1]))


        return ans if len(finished) == n else -1