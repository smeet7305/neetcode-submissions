class Solution:
    def dfs(self,isConnected,visited,node):
        visited.add(node)
        for neigh in range(len(isConnected)):
            if isConnected[node][neigh]==1 and neigh not in visited:
                
                self.dfs(isConnected,visited,neigh)

               

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=set()
        province=0
        for node in range(n):
            if node not in visited:
                self.dfs(isConnected,visited,node)
                province+=1 
        return province





