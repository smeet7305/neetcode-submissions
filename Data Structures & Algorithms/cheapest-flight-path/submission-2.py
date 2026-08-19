from collections import defaultdict
import sys
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist=[float('inf')]*n

        dist[src]=0
        for i in range(k+1):
            tmpdist=dist.copy()

            for u,v,w in flights:
                if dist[u]!=float('inf'):
                    tmpdist[v]=min(tmpdist[v],dist[u]+w)

            dist=tmpdist

        if dist[dst]!=float('inf'):
            return dist[dst]
        else:
            return -1




        