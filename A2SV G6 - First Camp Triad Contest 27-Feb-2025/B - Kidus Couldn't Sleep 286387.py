# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n, k = map(int, input().split())
arr = list(map(int, input().split()))
window = 0
for i in range(k):
    window += arr[i]
total = window
for right in range(k,n):
    window += arr[right]
    window -= arr[right-k]
    total += window
print(f"{total/(n-k+1):.6f}")