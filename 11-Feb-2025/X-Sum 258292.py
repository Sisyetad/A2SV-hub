# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())
for i in range(t):
    matrix = []
    n,m=map(int,input().split())
    for i in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
    primary_diagonal = {}
    secondary_diagonal = {}
    
    for row in range(n):
        for col in range(m):
            if row + col not in primary_diagonal :
                primary_diagonal[row + col] = 0
            if row - col not in secondary_diagonal:
                secondary_diagonal[row - col] = 0
            
            primary_diagonal[row + col] += matrix[row][col]
            secondary_diagonal[row - col] += matrix[row][col]
                
    max_sum = 0
    for i in range(n):
        for j in range(m):
            
            bishop_sum = primary_diagonal[i + j] + secondary_diagonal[i - j] - matrix[i][j]
            max_sum = max(max_sum, bishop_sum)
    
    print(max_sum)


