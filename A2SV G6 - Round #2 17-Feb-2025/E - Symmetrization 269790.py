# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

test = int(input())
for i in range(test):
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(input())
        matrix.append(row)
    operations = 0
    for i in range((n + 1) // 2): 
        for j in range(n // 2):
            a = matrix[i][j]
            b = matrix[j][n - i - 1]
            c = matrix[n - i - 1][n - j - 1]
            d = matrix[n - j - 1][i]
            ones = int(a) + int(b) + int(c) + int(d)
            operations += min(ones, 4 - ones)
    print(operations)