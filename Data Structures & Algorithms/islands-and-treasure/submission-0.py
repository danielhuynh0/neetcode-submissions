class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        seen = set()
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((0, r,c))
                    seen.add((r,c))
        
        while queue:
            dist, r, c = queue.popleft()
            grid[r][c] = dist

            if r > 0 and grid[r-1][c] == INF and (r-1,c) not in seen:
                queue.append((dist+1, r-1, c))
                seen.add((r-1, c))
            if c > 0 and grid[r][c-1] == INF and (r,c-1) not in seen:
                queue.append((dist+1, r, c-1))
                seen.add((r, c-1))
            if r < len(grid)-1 and grid[r+1][c] == INF and (r+1,c) not in seen:
                queue.append((dist+1, r+1, c))
                seen.add((r+1, c))
            if c < len(grid[0])-1 and grid[r][c+1] == INF and (r,c+1) not in seen:
                queue.append((dist+1, r, c+1))
                seen.add((r, c+1))