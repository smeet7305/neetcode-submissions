class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        idx=[[1,0],[0,1],[-1,0],[0,-1]]

        effort=[]
        for i in range(rows):
            r=[]
            for j in range(cols):
                r.append(float('inf'))
            
            effort.append(r)
        q=[]
        effort[0][0]=0
        heapq.heappush(q,(0,0,0))


        while q:
            cur_effort,r,c=heapq.heappop(q)

            if (r,c)==(rows-1,cols-1):
                return cur_effort
            
            
            for i,j in idx:
                nr=r+i
                nc=c+j


                if nr in range(rows) and nc in range(cols):
                    next_effort=abs(heights[nr][nc]-heights[r][c])
                    new_effort=max(cur_effort,next_effort)

                    if new_effort<effort[nr][nc]:
                        effort[nr][nc]=new_effort
                        heapq.heappush(q,(new_effort,nr,nc))



