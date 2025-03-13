# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = deque()
sets = set()
for i in range(n):
    if len(ans) >= k:
        if arr[i] not in sets:
            top = ans.pop()
            sets.remove(top)
            ans.appendleft(arr[i])
            sets.add(arr[i])
    elif arr[i] not in sets:
        ans.appendleft(arr[i])
        sets.add(arr[i])
print(len(ans))
print(*ans)