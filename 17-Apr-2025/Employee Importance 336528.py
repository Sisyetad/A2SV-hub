# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_map = {}
        for employee in employees:
            adj_map[employee.id] = (employee.importance, employee.subordinates)
        ans = 0
        def dfs(node):
            nonlocal ans
            ans += adj_map[node][0]
            for ngbr in adj_map[node][-1]:
                dfs(ngbr)
        dfs(id)
        return ans