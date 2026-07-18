import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        dist=[]
    
        for i in range(len(points)):
            dist.append(points[i][0]*points[i][0] + points[i][1]*points[i][1])
            heapq.heappush(heap,(dist[i],points[i]))
        
        while k:
            dis,pnt= heapq.heappop(heap)
            ans.append(pnt)
            k-=1
        return ans
        
    