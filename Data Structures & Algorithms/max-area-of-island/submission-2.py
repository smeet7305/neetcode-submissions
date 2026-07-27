class Solution:
    def dfs(self,rows,col,r,c,idx,area,grid):
        if r<0 or r>=rows or c<0 or c>=col or grid[r][c]==0:
            return 0
        
        grid[r][c]=0
        area=1
        for i,j in idx:
            area+=self.dfs(rows,col,r+i,c+j,idx,area,grid)

        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        idx=[[0,1],[1,0],[0,-1],[-1,0]]
        area=0
        maxarea=0
        for i in range(rows):
            for j in range(col):
                if grid[i][j]==1:
                    area=self.dfs(rows,col,i,j,idx,area,grid)
                maxarea=max(maxarea,area)
        return maxarea