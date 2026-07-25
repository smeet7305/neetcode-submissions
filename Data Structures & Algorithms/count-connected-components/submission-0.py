class Solution:
    def dfs(self,adj,visited,node):
        if node not in visited:
            visited.add(node)
        for i in adj[node]:
            if i not in visited:
                self.dfs(adj,visited,i)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        count=0
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                self.dfs(adj,visited,i)
                count+=1
            
        return count

