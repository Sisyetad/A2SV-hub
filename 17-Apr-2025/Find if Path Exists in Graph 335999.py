# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list  = [[] for i in range(n)]
        for v, u  in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            for ngbr in adj_list[node]:
                if ngbr not in visited:
                    if dfs(ngbr):
                        return True
                    
            return False
        return dfs(source)