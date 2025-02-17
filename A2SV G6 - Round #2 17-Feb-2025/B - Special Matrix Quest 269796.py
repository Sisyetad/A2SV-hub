# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
Sum = 0
for f in range(n):
    for j in range(n):
        if f == j:
            Sum += matrix[f][j]
        if f == j:
            Sum += matrix[f][-j-1]
        if j == (n-1)//2:
            Sum += matrix[f][j]
        if f == (n-1)//2:
            Sum += matrix[f][j]
Sum -= (3*matrix[(n-1)//2][(n-1)//2])
print(Sum)