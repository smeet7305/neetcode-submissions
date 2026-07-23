from collections import defaultdict

class Solution:

    def dfs(self, node, parent, adj, visited):
        visited.add(node)

        for neigh in adj[node]:

            # Ignore the edge we came from
            if neigh == parent:
                continue

            # Found a back edge -> cycle
            if neigh in visited:
                return True

            if self.dfs(neigh, node, adj, visited):
                return True

        return False

    def findRedundantConnection(self, edges):
        adj = defaultdict(list)

        for u, v in edges:

            # Add the current edge
            adj[u].append(v)
            adj[v].append(u)

            visited = set()

            # If a cycle is formed, return this edge
            if self.dfs(u, -1, adj, visited):
                return [u, v]