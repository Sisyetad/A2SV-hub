# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
for j in range(t):
    n, m = map(int, input().split())
    prefix_sum = list(map(int, input().split()))
    
    prefix_sum.insert(0,0)
    for i in range(1,n+1):
        prefix_sum[i] += prefix_sum[i-1]
    
    for _ in range(m):
        l, r, k = map(int, input().split())
        total_sum = prefix_sum[-1] - (prefix_sum[r] - prefix_sum[l-1]) + ((r-l+1)*k)
        if total_sum%2:
            print("YES")
        else:
            print("NO")
    