# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
arr = list(map(int, input().split()))
arr1 = arr[:]
arr.sort()
arr.insert(0,0)
arr1.insert(0,0)
for i in range(1,n+1):
    arr1[i] += arr1[i-1]
    arr[i] += arr[i-1]
m = int(input())

for i in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(arr1[r] - arr1[l-1])
    else:
        print(arr[r] - arr[l-1])