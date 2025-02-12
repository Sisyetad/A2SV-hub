# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
index = 0
ans = []
for i in arr2:
    while index < n and i > arr1[index]:
        index += 1
    ans.append(index)
print(*ans)