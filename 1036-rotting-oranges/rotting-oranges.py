class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        def isBound(c,r):
            return ((c>=0 and c<len(grid)) and (r>=0 and r<len(grid[0])))
        rotten = deque()
        visited = set()
        for c in range(len(grid)):
            for r in range(len(grid[c])):
                if grid[c][r] == 2:
                    rotten.append((c,r))
                    visited.add((c,r))
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        minutes = 0
        while(rotten):
            breadth = set()
            while(rotten):
                c,r = rotten.popleft()
                for d in directions:
                    nc, nr = c + d[0], r + d[1]
                    if isBound(nc,nr) and (nc,nr) in visited:
                        continue
                    if isBound(nc,nr):
                        if grid[nc][nr] == 1:
                            grid[nc][nr]=2
                            breadth.add((nc,nr))
            if not breadth:
                for row in grid:
                    if 1 in row:
                        return -1
                return minutes
            for b in breadth - visited:
                rotten.append(b)
                visited.add(b)
            minutes+=1
        for row in grid:
            if 1 in row:
                return -1
        return minutes

