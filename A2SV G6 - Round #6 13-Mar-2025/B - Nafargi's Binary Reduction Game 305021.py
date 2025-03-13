# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

n = int(input())
s = input()
stack = []
for i in range(n):
    if s[i] == '0':
        if stack and stack[-1] == '1':
            stack.pop()
        else:
            stack.append(s[i])
    else:
        if stack and stack[-1] == '0':
            stack.pop()
        else:
            stack.append(s[i])
print(len(stack))