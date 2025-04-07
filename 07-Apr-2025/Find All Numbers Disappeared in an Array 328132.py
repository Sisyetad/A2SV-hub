# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark numbers that are present
        for i in range(len(nums)):
            # Find the correct index for the current number (adjusted for 1-based index)
            index = abs(nums[i]) - 1
            
            # Mark the element at this index as negative if it is positive
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: Collect missing numbers
        result = []
        for i in range(len(nums)):
            # If the number at index i is positive, it means (i + 1) is missing
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
