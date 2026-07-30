class Solution:
    def dfs(self,rows,col,r,c,grid,idx):
        if r<0 or r>=rows or c<0 or c>=col or grid[r][c]==0:
            return 0

        grid[r][c]=2 #marked visited
        neigh=0
        for i,j in idx:
            if 0<=r+i<rows and 0<=c+j<col:
                if grid[r+i][c+j]==1 or grid[r+i][c+j]==2:
                    neigh+=1
        
        perimeter=4-neigh

        for i,j in idx:
            if 0<=r+i<rows and 0<=c+j<col and grid[r+i][c+j]==1:
                perimeter+=self.dfs(rows,col,r+i,c+j,grid,idx)

        return perimeter


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        idx=[[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(rows):
            for j in range(col):
                if grid[i][j]==1:
                    return self.dfs(rows,col,i,j,grid,idx)
                continue
                