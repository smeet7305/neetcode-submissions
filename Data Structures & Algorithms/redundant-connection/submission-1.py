class Solution:
    def dfs(self,node,parent,adj,visited):
        visited.add(node)
        for neigh in adj[node]:
            if neigh==parent:
                continue
            
            if neigh in visited:
                return True
            
            if self.dfs(neigh,node,adj,visited):
                return True

        return False


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
            visited=set()
            if self.dfs(u,-1,adj,visited):
                return [u,v]