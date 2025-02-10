# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #bubble sort
        n = len(heights)
        i = 0
        while i < n:
            Sorted = False
            j = 0
            while j < n-i-1:
                if heights[j+1] > heights[j]:
                    heights[j+1],heights[j] = heights[j],heights[j+1]
                    names[j+1],names[j] = names[j],names[j+1]
                    Sorted = True
                j += 1
            if not Sorted:
                return names
            i += 1
        return names