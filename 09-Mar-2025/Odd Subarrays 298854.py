# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mono_stack = []
    ans = 0
    for i in range(n):
        if mono_stack and mono_stack[-1] < arr[i]:
            mono_stack.pop()
            
        mono_stack.append(arr[i])
        if len(mono_stack) == 2:
            ans += 1
            mono_stack = []
    print(ans)