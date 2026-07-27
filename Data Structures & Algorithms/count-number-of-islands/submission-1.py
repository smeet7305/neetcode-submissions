class Solution:
    def dfs(self,rows,col,idx,r,c,grid):
        if r<0 or r>=rows or c<0 or c>=col or grid[r][c]=="0":
            return 
        
        grid[r][c]="0"
        for i,j in idx:
            self.dfs(rows,col,idx,r+i,c+j,grid)



    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        idx=[[1,0],[-1,0],[0,-1],[0,1]]
        count=0

        for i in range(rows):
            for j in range(col):
                if grid[i][j]=="1":
                    self.dfs(rows,col,idx,i,j,grid)
                    count+=1
        
        return count

        