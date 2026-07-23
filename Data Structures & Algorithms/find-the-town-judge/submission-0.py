class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg=[0]*(n+1)
        outdeg=[0]*(n+1)
        for u,v in trust:
            outdeg[u]+=1
            indeg[v]+=1
        
        for i in range(1,n+1):
            if outdeg[i]==0 and indeg[i]==n-1:
                return i
        
        return -1