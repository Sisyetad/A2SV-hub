# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
t = input()
ans=""
i=0
size = 1
while i < n:
    ans += t[i]
    i += size
    size += 1
print(ans)