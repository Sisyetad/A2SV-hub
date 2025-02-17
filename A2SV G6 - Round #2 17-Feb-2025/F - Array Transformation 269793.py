# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
test = int(input())
for i in range(test):
    n = int(input())
    ans = n
    arr = list(map(int,input().split()))
    arr = Counter(arr)
    arr = sorted(arr.items(), key = lambda x: x[1])
    for i in range(len(arr)):
        ans = min(ans,n-(len(arr)-i)*arr[i][1])
    print(ans)