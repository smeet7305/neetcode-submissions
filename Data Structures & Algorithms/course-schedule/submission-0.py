class Solution:
    def hasNoCycle(self,node,adj,visited,path):
        if node in visited:
            return True
        if node in path:
            return False
        
        path.add(node)

        for i in adj[node]:
            if not self.hasNoCycle(i,adj,visited,path): #i visited all the neighbouring nodes and found no cycle
                return False
        path.remove(node)
        visited.add(node)
        return True
        



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[pre].append(course)

        path=set()
        visited=set()
        for course in range(numCourses):
            if not self.hasNoCycle(course, adj, visited, path):
                return False

        return True