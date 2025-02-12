# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l,r=0,n-1
        ans=[]
        Sum=0
        while(l<r):
            Sum=numbers[l]+numbers[r]
            if(Sum<target):
                l+=1
            elif(Sum>target):
                r-=1
            else:
                ans.append(l+1)
                ans.append(r+1)
                return ans