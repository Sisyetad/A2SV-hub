# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    stack = []
    ans = deque()
    for i in range(n):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        stack.append(arr[i])
        if stack[0] >= arr[i]:
            ans.appendleft(arr[i])
        else:
            ans.append(arr[i])
    print(*ans)