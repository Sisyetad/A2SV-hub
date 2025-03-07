# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
arr = list(map(int, input().split()))
diff = []
for i in range(n-1):
    diff.append((arr[i+1] - arr[i],i))
    
diff.sort()
total = arr[-1] - arr[0]
for i in range(1,k):
    total -= diff[-i][0]
print(total)