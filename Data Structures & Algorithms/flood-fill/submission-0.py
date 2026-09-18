class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        idx=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()

        cur_color=image[sr][sc]

        image[sr][sc]=color
        q.append((sr,sc))
        if cur_color == color:
            return image

        while q:
            r,c =q.popleft()

            for i,j in idx:
                nr=r+i
                nc=c+j
                if(nr in range(rows) and nc in range(cols) and image[nr][nc]==cur_color):
                    image[nr][nc]=color
                    q.append((nr,nc))
        
        return image

                
