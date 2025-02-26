# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
arr = list(map(int, input().split()))
p_diff = [0]*n
s_diff = [0]*n
for i in range(1,n):
    if arr[i-1] > arr[i]:
        p_diff[i] = arr[i-1] - arr[i]
        
    else:
        p_diff[i] = 0
for i in range(2,n+1):    
    if arr[-i] < arr[-i+1]:
        s_diff[-i] = arr[-i+1] - arr[-i]
    else:
        s_diff[-i] = 0

for i in range(1,n):
    p_diff[i] += p_diff[i-1]
    s_diff[-i-1] += s_diff[-i]
for q in range(m):
    start, end = map(int, input().split())
    if start < end:
        print(p_diff[end-1] - p_diff[start-1])
    else:
        print(s_diff[end-1] - s_diff[start-1])