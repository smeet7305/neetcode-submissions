class Solution:

    def dfs(self,idx,rows,cols,grid,r,c):
        if(r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0"):
            return;
        
        grid[r][c]="0"
        for i,j in idx:
            self.dfs(idx,rows,cols,grid,r+i,c+j)

        


    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid);
        cols=len(grid[0])
        idx=[[1,0],[0,1],[-1,0],[0,-1]]
        count=0

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]=="1"):
                    self.dfs(idx,rows,cols,grid,i,j)
                    count+=1
        
        return count;