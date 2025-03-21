# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

n, x = map(int, input().split())
dis = 0
for _ in range(n):
    oper, val = input().split()
    if oper == '-':
        if int(val) <= x:
            x -= int(val)
        else:
            dis += 1
    else:
        x += int(val)
print(x, dis)