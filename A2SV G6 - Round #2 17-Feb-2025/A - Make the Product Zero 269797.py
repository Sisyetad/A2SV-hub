# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

n = map(int,input().split())
arr = list(map(int,input().split()))
Min = abs(arr[0])
for i in range(1,len(arr)):
    Min = min(Min,abs(arr[i]))
print(Min)