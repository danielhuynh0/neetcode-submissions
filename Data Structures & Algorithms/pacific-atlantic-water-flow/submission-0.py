class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific
        pacific = set() # can flow into pacific
        queue = deque()
        for c in range(len(heights[0])):
            queue.append((0, c))
            pacific.add((0, c))
        for r in range(len(heights)):
            queue.append((r, 0))
            pacific.add((r, 0))
        
        while queue:
            r,c = queue.popleft()

            cur_height = heights[r][c]
            if r > 0 and (r-1,c) not in pacific and cur_height <= heights[r-1][c]:
                queue.append((r-1,c))
                pacific.add((r-1, c))
            if c > 0 and (r,c-1) not in pacific and cur_height <= heights[r][c-1]:
                queue.append((r,c-1))
                pacific.add((r, c-1))
            if r < len(heights)-1 and (r+1,c) not in pacific and cur_height <= heights[r+1][c]:
                queue.append((r+1,c))
                pacific.add((r+1, c))
            if c < len(heights[0])-1 and (r,c+1) not in pacific and cur_height <= heights[r][c+1]:
                queue.append((r,c+1))
                pacific.add((r, c+1))
        
        # atlantic
        atlantic = set()
        queue = deque()
        for c in range(len(heights[0])):
            queue.append((len(heights)-1, c))
            atlantic.add((len(heights)-1, c))
        for r in range(len(heights)):
            queue.append((r, len(heights[0])-1))
            atlantic.add((r, len(heights[0])-1))
        
        while queue:
            r,c = queue.popleft()

            cur_height = heights[r][c]
            if r > 0 and (r-1,c) not in atlantic and cur_height <= heights[r-1][c]:
                queue.append((r-1,c))
                atlantic.add((r-1, c))
            if c > 0 and (r,c-1) not in atlantic and cur_height <= heights[r][c-1]:
                queue.append((r,c-1))
                atlantic.add((r, c-1))
            if r < len(heights)-1 and (r+1,c) not in atlantic and cur_height <= heights[r+1][c]:
                queue.append((r+1,c))
                atlantic.add((r+1, c))
            if c < len(heights[0])-1 and (r,c+1) not in atlantic and cur_height <= heights[r][c+1]:
                queue.append((r,c+1))
                atlantic.add((r, c+1))

        return [[r,c] for r,c in pacific & atlantic]
