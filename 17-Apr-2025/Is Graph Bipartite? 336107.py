# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for i in range(n)]
        
        def dfs(node):
            temp = True
            for ngbr in graph[node]:
                if color[ngbr] == -1:
                    if color[node] == 0:
                        color[ngbr] = 1
                    else:
                        color[ngbr] = 0
                    temp = temp and dfs(ngbr)
                elif color[ngbr] == color[node]:
                    return False
            return temp

        result = True
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                result = result and dfs(node)
        return result