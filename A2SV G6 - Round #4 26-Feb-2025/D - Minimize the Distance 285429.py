# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
arr.sort()
if n % 2:
    target = arr[n//2]
else:
    target = (arr[(n//2)-1])
print(target)
    