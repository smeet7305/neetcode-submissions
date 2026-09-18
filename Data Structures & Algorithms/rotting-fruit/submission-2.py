class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        idx=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()
        fresh=0
        minutes=0

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==1):
                    fresh+=1
                elif(grid[i][j]==2):
                    q.append((i,j))
        
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for i,j in idx:
                    nr=r+i
                    nc=c+j

                    if(nr in range(rows) and nc in range(cols) and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
                
            minutes+=1
        
        if(fresh!=0): return -1
        else: return minutes
