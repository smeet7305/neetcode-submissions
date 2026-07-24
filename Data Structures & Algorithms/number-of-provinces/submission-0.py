class Solution:
    def dfs(self,adj,visited,node):
        visited.add(node)
        for i in adj[node]:
            if i not in visited:
                self.dfs(adj,visited,i)
               

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    adj[i].append(j)
        

        visited=set()
        province=0
        for node in range(len(adj)):
            if node not in visited:
                self.dfs(adj,visited,node)
                province+=1 
        return province





