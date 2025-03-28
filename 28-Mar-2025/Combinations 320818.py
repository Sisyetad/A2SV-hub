# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n + 1)]
        combinations = []
        
        def backtrack(indx, combination): 
            if len(combination) == k:
                combinations.append(combination[:])
                return 
                
            for i in range(indx,len(nums)):
                combination.append(nums[i])
                backtrack(i + 1, combination)
                combination.pop()
            
        backtrack(0, [])
        return combinations