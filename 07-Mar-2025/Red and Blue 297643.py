# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    maxs1 = maxs2 = 0
    prefix1 = prefix2 = 0
    for i in range(n):
        prefix1 += a[i]
        maxs1 = max(maxs1, prefix1)
    for j in range(m):
        prefix2 += b[j]
        maxs2 = max(maxs2, prefix2)
    print(maxs1 + maxs2)