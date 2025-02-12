# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
l, r = 0, 0
ans = []
while l < n and r < m:
    if arr1[l] < arr2[r]:
        ans.append(arr1[l])
        l += 1
    else:
        ans.append(arr2[r])
        r += 1
if n > l:
    ans.extend(arr1[l:])
else:
    ans.extend(arr2[r:])
print(*ans)