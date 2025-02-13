# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
arr = list(map(int, input().split()))
window = 0
left = 0
size = 0
for right in range(n):
    window += arr[right]
    while window > s:
        window -= arr[left]
        left += 1
    
    size = max(size, right - left + 1)
print(size)