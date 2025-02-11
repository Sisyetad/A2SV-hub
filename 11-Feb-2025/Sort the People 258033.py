# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(1, n):
            key_height = heights[i]
            key_name = names[i]
            j = i - 1

            while j >= 0 and heights[j] < key_height:
                j -= 1
            heights.pop(i)
            names.pop(i)
            heights.insert(j+1,key_height)
            names.insert(j+1,key_name)   

        return names
