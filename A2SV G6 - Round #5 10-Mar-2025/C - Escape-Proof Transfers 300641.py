# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n, t, c = map(int, input().split())
arr = list(map(int, input().split()))
count = ans = 0
right = 0
while right < n:
    if  arr[right] <= t:
        count += 1
    else:
        count = 0
    
    if count >= c:
        ans += 1
    right += 1
print(ans)