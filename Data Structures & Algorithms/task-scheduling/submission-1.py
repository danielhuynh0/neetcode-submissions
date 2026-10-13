class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        waiting = deque()
        task_heap = [(count, task) for task, count in counts.items()]
        heapq.heapify_max(task_heap)
        cycles = 0
        while task_heap or waiting:
            cycles += 1
            if waiting and waiting[0][0] <= cycles: 
                wait_time, itm = waiting.popleft()
                heapq.heappush_max(task_heap, (counts[itm], itm)) # technically, as task_heap max size is 26, O(1)

            cur = None
            if len(task_heap) > 0:
                cur_count, cur = heapq.heappop_max(task_heap)
                counts[cur] = counts[cur] - 1
                if counts[cur] == 0:
                    del counts[cur]
                else:
                    if n > 0:
                        waiting.append([n+cycles+1, cur])
                    else:
                        heapq.heappush_max(task_heap, (counts[cur], cur))
        return cycles