class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        done = set()
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in done:
                    continue
                if grid[r][c] == 0:
                    continue
                queue.append((r,c))
                visited = set()
                visited.add((r,c))
                while queue:
                    r,c = queue.popleft()
                    if c > 0 and (r, c-1) not in visited and grid[r][c-1] == 1:
                        queue.append((r, c-1))
                        visited.add((r,c-1))
                    if r > 0 and (r-1, c) not in visited and grid[r-1][c] == 1:
                        queue.append((r-1, c))
                        visited.add((r-1,c))
                    if c < len(grid[0])-1 and (r, c+1) not in visited and grid[r][c+1] == 1:
                        queue.append((r, c+1))
                        visited.add((r,c+1))
                    if r < len(grid)-1 and (r+1, c) not in visited and grid[r+1][c] == 1:
                        queue.append((r+1, c))
                        visited.add((r+1,c))
                ans = max(ans, len(visited))
                done.update(visited)
        return ans


        
        # def dfs(r, c, cur_set):
        #     if grid[r][c] == 1:
        #         cur_set.add((r,c))
        #     if c > 0 and (r,c-1) not in cur_set and grid[r][c-1] != 0:
        #         dfs(r, c-1, cur_set)
        #     if r > 0 and (r-1,c) not in cur_set and grid[r-1][c] != 0:
        #         dfs(r-1, c, cur_set)
        #     if r < len(grid) - 1 and (r+1,c) not in cur_set and grid[r+1][c] != 0:
        #         dfs(r+1, c, cur_set)
        #     if c < len(grid[0]) - 1 and (r,c+1) not in cur_set and grid[r][c+1] != 0:
        #         dfs(r, c+1, cur_set)
        
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 0:
        #             continue
        #         if (r,c) in seen:
        #             continue
        #         result = set()
        #         dfs(r, c, result)
        #         ans = max(ans, len(result))
        #         seen.update(result)
        # return ans
            
            

