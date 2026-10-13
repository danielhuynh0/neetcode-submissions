class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        done = set()

        for e in edges:
            s = e[0]
            d = e[1]
            adj[s].append(d)
            adj[d].append(s)

        ans = 0

        for i in range(n):
            if i in done:
                continue
            queue = deque()
            queue.append(i)
            done.add(i)
            while queue:
                node = queue.popleft()
                children = adj[node]
                for c in children:
                    if c in done:
                        continue
                    queue.append(c)
                    done.add(c)
            ans += 1

        return ans



        
