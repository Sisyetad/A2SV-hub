# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
s = input()
from collections import defaultdict
def numSubarraysWithSum(nums, goal):
        prefix_count = defaultdict(int)  
        prefix_count[0] = 1  
        
        prefix_sum = 0
        result = 0
        
        for num in nums:
            prefix_sum += int(num) 
            
            if (prefix_sum - goal) in prefix_count:
                result += prefix_count[prefix_sum - goal]
            
            prefix_count[prefix_sum] += 1  
        
        return result

 
print(numSubarraysWithSum(s,k))