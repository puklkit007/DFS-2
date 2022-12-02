from queue import Queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # DFS
        self.m = len(grid)
        self.n = len(grid[0])
        self.count = 0
        
        self.directions = [(-1, 0 ), (1, 0), (0, -1), (0, 1)] #UpDownLeftRight        
                    
        
        def dfs(r, c):
            if r >= 0 and r < self.m and c >= 0 and c < self.n and grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return
            
            for dir in self.directions:
                nr = r + dir[0]
                nc = c + dir[1]
                dfs(nr, nc)
            
            
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    self.count += 1
        return self.count
    
    
        # BFS
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        directions = [(-1, 0 ), (1, 0), (0, -1), (0, 1)] #UpDownLeftRight
        
        q = Queue()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    q.put((i, j))            
                    count += 1
            
                    while not q.empty():
                        curr = q.get()

                        for dir in directions:
                            nr = curr[0] + dir[0]
                            nc = curr[1] + dir[1]
                            if nr >= 0 and nr < m and nc >=0 and nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.put((nr, nc))        
                    
        return count
            
            
                    
