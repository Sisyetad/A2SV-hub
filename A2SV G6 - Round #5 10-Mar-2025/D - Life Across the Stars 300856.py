# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict
n = int(input())
prefix = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    prefix[a] += 1
    prefix[b] -= 1

max_alive = 0
current = 0
best = float("inf")
for i in sorted(prefix):
    current += prefix[i]
    if current > max_alive:
        max_alive = current
        best = i
print(best, max_alive)