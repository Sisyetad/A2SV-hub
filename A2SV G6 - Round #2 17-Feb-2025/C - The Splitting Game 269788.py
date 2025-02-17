# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = [i for i in input()]
    suffix = Counter(s)
    prefix = set()
    max_str = 0
    for i in s:
        prefix.add(i)
        if suffix[i] > 1:
            suffix[i] -= 1
        else:
            suffix.pop(i)
        max_str = max(max_str,len(suffix) + len(prefix))
    print(max_str)