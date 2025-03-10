# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

# Multiple test cases
t = int(input())
for _ in range(t):
    input()
    n, k = map(int,input().split())
    arr = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    
    result = [float("inf")] * n
    for i in range(k):
        result[arr[i]-1] = temp[i]
    for i in range(1,n):
        result[i] = min(result[i], result[i-1] + 1)
    for i in range(2,n+1):
        result[-i] = min(result[-i], result[-i+1]+1)
    print(*result)