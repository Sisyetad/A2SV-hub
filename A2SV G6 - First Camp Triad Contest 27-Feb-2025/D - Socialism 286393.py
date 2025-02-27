# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

test = int(input())
for _ in range(test):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    total = sum(arr)
    left = 0
    while n > 0 and total/n < x:
        total -= arr[left]
        n -= 1
    print(n)