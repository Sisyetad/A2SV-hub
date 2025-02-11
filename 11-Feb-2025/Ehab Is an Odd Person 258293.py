# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input()) 
nums = list(map(int,input().split()))
even, odd = False, False
for i in range(n):
    if nums[i]%2:
        odd = True
    else:
        even = True
        
if even and odd:
    nums.sort()
print(*nums)