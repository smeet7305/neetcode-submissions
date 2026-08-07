class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        idx=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        q=deque()
        if grid[0][0]==1 or grid[rows-1][cols-1]==1: return -1

        q.append((0,0))
        grid[0][0]=1
        
        while q:
            r,c=q.popleft()
            for i,j in idx:
                nr=r+i
                nc=c+j
                if nr in range(rows) and nc in range(cols) and grid[nr][nc]==0:
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr,nc))
        
        if grid[rows-1][cols-1]==0:
            return -1
        else:
            return grid[rows-1][cols-1]

