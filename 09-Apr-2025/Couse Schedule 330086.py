# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            
        white = 0
        gray = 1
        black = 2
        color = {course: white for course in range(numCourses)}
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
            
            color[node] = gray
            for ngbr in adj_list[node]:
                if color[ngbr] == white:
                    dfs(ngbr)
                
                elif color[ngbr] == gray:
                    no_cycle = False
            color[node] = black


        for course in range(numCourses):
            if color[course] == white:
                dfs(course)
                
        return no_cycle