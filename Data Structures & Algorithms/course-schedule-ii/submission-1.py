class Solution:

    def dfs(self,visited,adj,node,stack,path):
        visited.add(node)
        path.add(node)
        for neigh in adj[node]:
            if neigh not in visited:
                if self.dfs(visited,adj,neigh,stack,path):
                    return True
            elif neigh in path:
                return True
        
        path.remove(node)
        stack.append(node)
        return False


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)

        visited=set()
        path=set()
        stack=[]
        for i in range(numCourses):
            if i not in visited:
                if self.dfs(visited,adj,i,stack,path):
                    return []

        return stack[::-1]