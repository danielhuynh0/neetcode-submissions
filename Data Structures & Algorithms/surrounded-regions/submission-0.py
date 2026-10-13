class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def is_edge(r, c):
            return r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1
        
        sources = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    sources.append((r,c))
        
        seen = set()
        for source in sources:
            r,c = source
            if (r,c) in seen or board[r][c] != 'O':
                continue
            queue = deque()
            queue.append(source)
            seen.add(source)

            region = set()
            is_surrounded = True
            while queue:
                r,c = queue.popleft()
                region.add((r,c))

                if is_edge(r,c):
                    is_surrounded = False

                if r > 0 and (r-1,c) not in region and board[r-1][c] == 'O':
                    queue.append((r-1,c))
                    region.add((r-1,c))
                if c > 0 and (r,c-1) not in region and board[r][c-1] == 'O':
                    queue.append((r,c-1))
                    region.add((r,c-1))
                if r < len(board)-1 and (r+1,c) not in region and board[r+1][c] == 'O':
                    queue.append((r+1,c))
                    region.add((r+1,c))
                if c < len(board[0])-1 and (r,c+1) not in region and board[r][c+1] == 'O':
                    queue.append((r,c+1))
                    region.add((r,c+1))
            if is_surrounded:
                for r,c in region:
                    board[r][c] = 'X'
            seen |= region