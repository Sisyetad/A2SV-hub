# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_map = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    adj_map[i].append(j)
        
        visited = [False for i in range(n)]
        print(visited)
        def dfs(node):
            visited[node] = True
            for ngbr in adj_map[node]:
                if not visited[ngbr]:
                    dfs(ngbr)
        
        ans = 0
        for node in range(n):
            if not visited[node]:
                ans += 1
                dfs(node)
        return ans