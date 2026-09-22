class Solution:
    def dfs(self,rows,cols,idx,r,c,grid):
        if(r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0"):
            return
        
        grid[r][c]="0"
        for i,j in idx:
            nr=r+i
            nc=c+j
            self.dfs(rows,cols,idx,nr,nc,grid)      


    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        idx=[[0,1],[1,0],[-1,0],[0,-1]]
        count=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    self.dfs(rows,cols,idx,i,j,grid)
                    count+=1
        return count
        
