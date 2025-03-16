# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
queue_min = deque() 
queue_max = deque() 
left = 0

for right, curr in enumerate(arr):
    while queue_min and queue_min[-1][1] > curr:
        queue_min.pop()
    queue_min.append((right, curr))

    while queue_max and queue_max[-1][1] < curr:
        queue_max.pop()
    queue_max.append((right, curr))

    while queue_max[0][1] - queue_min[0][1] > k:
        left += 1
        if queue_min[0][0] < left:
            queue_min.popleft()
        if queue_max[0][0] < left:
            queue_max.popleft()

    count += (right - left + 1)

print(count)
