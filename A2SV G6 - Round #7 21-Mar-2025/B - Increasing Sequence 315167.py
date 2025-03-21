# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    num = 1 if arr[0] != 1 else 2
    ans.append(num)
    for i in range(1, n):
        if ans[i-1] + 1 != arr[i]:
            ans.append(ans[i-1] + 1)
        else:
            ans.append(arr[i] + 1)
        
    print(ans.pop())