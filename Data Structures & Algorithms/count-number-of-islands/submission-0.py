class Solution:
    def dfs(self,r,c,rows,col,dirn,grid):
        if (r<0 or r>=rows or c<0 or c>=col or grid[r][c]=="0"):
            return
        
        grid[r][c]="0"
        for i,j in dirn:
            self.dfs(r+i,c+j,rows,col,dirn,grid)
        


    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        count=0
        dirn=[[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(rows):
            for j in range(col):
                if grid[i][j]=="1":
                    self.dfs(i,j,rows,col,dirn,grid)
                    count+=1
        
        return count