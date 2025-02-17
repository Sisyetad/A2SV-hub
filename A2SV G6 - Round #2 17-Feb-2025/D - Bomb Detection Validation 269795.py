# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(input().split())
flag = False
for row in range(n):
    for col in range(m):
        Sum = 0
        if arr[row][0][col] == '*':
            continue
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if 0 <= i < n and 0 <= j < m:
                    if arr[i][0][j] == '*':
                        Sum += 1
        if (arr[row][0][col] != f'{Sum}'):
            if (Sum == 0 and arr[row][0][col] == '.'):
                continue
            else:
                print("NO")
                flag = True
                break
    if flag:
        break
if not flag:
    print("YES")