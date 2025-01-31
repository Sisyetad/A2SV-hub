# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

n = int(input())
for i in range(n):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] != "codeforces"[i]:
            count += 1
    print(count)