# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort()
ranges = 200002
prefix = [0] * ranges
for i,j in arr:
    prefix[i] += 1
    if j + 1 <= ranges:
        prefix[j + 1] -= 1
for i in range(1,ranges):
    prefix[i] += prefix[i-1]
for i in range(ranges):
    if prefix[i] >= k:
        prefix[i] = 1
    else:
        prefix[i] = 0
for i in range(1,ranges):
    prefix[i] += prefix[i-1]
for i in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a-1])