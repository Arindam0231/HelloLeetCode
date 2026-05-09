class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque
        rows, cols = len(maze), len(maze[0])

        def isExit(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            return (i == 0 or i == rows-1 or j == 0 or j == cols-1) and maze[i][j] == "."

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = deque([entrance])
        visited = {tuple(entrance)}
        step = 0

        while queue:
            step += 1
            for _ in range(len(queue)):       # process full level
                c, r = queue.popleft()        # BFS: FIFO
                for d in directions:
                    nc, nr = c + d[0], r + d[1]
                    if (nc, nr) in visited:
                        continue
                    if isExit(nc, nr):
                        return step
                    if 0 <= nc < rows and 0 <= nr < cols and maze[nc][nr] == ".":
                        visited.add((nc, nr))
                        queue.append((nc, nr))

        return -1