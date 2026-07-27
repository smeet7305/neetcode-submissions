class Solution:
    def dfs(self,grid,rows,col,r,c,area,idx):
        if r<0 or r>=rows or c<0 or c>=col or grid[r][c]==0:
            return 0
        
        grid[r][c]=0
        area=1
        for i,j in idx:
            area+=self.dfs(grid,rows,col,r+i,c+j,area,idx)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        idx=[[1,0],[0,1],[-1,0],[0,-1]]
        ans=0
        area=0
        for i in range(rows):
            for j in range(col):
                if grid[i][j]==1:
                    ans=max(ans,self.dfs(grid,rows,col,i,j,area,idx))
        
        return ans
