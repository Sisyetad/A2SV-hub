# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
window = 0
ans = 0
for right in range(n):
    window += arr[right]
    while window > t:
        window -= arr[left]
        left += 1
    ans = max(ans,right - left + 1)
print(ans)