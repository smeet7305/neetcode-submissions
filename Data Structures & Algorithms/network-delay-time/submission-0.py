from collections import defaultdict
import heapq
import sys
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        dist=[sys.maxsize]*(n+1)
        dist[k]=0
        for u,v,w in times:
            adj[u].append((v,w))
        
        q=[]
        heapq.heappush(q,(0,k))

        while q:
            d,node=heapq.heappop(q)

            if d>dist[node]:
                continue

            for neigh,w in adj[node]:
                if dist[neigh]>dist[node]+w:
                    dist[neigh]=dist[node]+w
                    heapq.heappush(q,(dist[neigh],neigh))
                    
        if sys.maxsize in dist[1:]:
            return -1
        else:
            return max(dist[1:])