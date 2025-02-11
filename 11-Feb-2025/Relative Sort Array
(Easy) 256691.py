# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diction = defaultdict(list)
        arr1 = sorted(arr1)
        for i in arr2:
            diction[i] = 0
        for i in arr1:
            if i not in diction:
                diction[i] = 0
            diction[i] += 1
        index = 0
        for i in diction:
            while diction[i]:
                arr1[index] = i
                if diction[i]:
                    diction[i] -= 1
                else:
                    diction.pop(i)
                index += 1
        return arr1