# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

# Multiple test cases
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    def solve(n, arr):
        pref = 0
        mono_stack = []
        for i in range(n):
            while mono_stack and mono_stack[-1][0] <= arr[i]:
                top = mono_stack.pop()
                if (pref - top[-1]) > 0:
                    return False
            mono_stack.append((arr[i],pref))
            pref += arr[i]
        return True
    
    ans1 = solve(n,arr)
    ans2 = solve(n,arr[::-1])
    if ans1 and ans2:
        print("YES")
    else:
        print("NO")