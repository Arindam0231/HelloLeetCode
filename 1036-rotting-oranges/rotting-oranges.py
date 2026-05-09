class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0

        for c in range(rows):
            for r in range(cols):
                if grid[c][r] == 2:
                    rotten.append((c, r))
                elif grid[c][r] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        minutes = 0

        while rotten and fresh:
            minutes += 1
            for _ in range(len(rotten)):       # process current level only
                c, r = rotten.popleft()
                for dc, dr in directions:
                    nc, nr = c + dc, r + dr
                    if 0 <= nc < rows and 0 <= nr < cols and grid[nc][nr] == 1:
                        grid[nc][nr] = 2       # grid mutation = visited
                        fresh -= 1             # O(1) fresh tracking
                        rotten.append((nc, nr))

        return minutes if fresh == 0 else -1

