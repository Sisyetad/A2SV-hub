# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
size = 0
window = Counter()
for right in range(n):
    window[arr[right]] += 1
    while len(window) > k:
        window[arr[left]] -= 1
        if window[arr[left]] == 0:
            del window[arr[left]]
        left += 1
    if size < right - left + 1:
        size = right - left + 1
        ans = [left + 1, right + 1]
print(*ans)