class Solution:

    def dfs(self,node,visited,pathvisited,adj,st):
        visited.add(node)
        pathvisited.add(node)
        for neigh in adj[node]:
            if neigh not in visited:
                if self.dfs(neigh,visited,pathvisited,adj,st):
                    return True
                
            else:
                if neigh in pathvisited:
                    return True

        pathvisited.remove(node)
        st.append(node)
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        
        visited=set()
        pathvisited=set()
        st=[]
        for i in range(numCourses):
            if i not in visited:
                if self.dfs(i,visited,pathvisited,adj,st): #if cycle contains then return [] ??
                    return []
        return st[::-1]



        