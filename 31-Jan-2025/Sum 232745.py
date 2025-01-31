# Problem: Sum - https://codeforces.com/contest/1742/problem/A

n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    arr.sort()
    if arr[0] + arr[1] == arr[2]:
        print("YES")
    else:
        print("NO")