# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

test = int(input())
for _ in range(test):
    n = int(input())
    a = list(map(int, input().strip()))
    b = list(map(int, input().strip()))
    prefix = a[:]
    for i in range(1,n):
        prefix[i] += prefix[i-1]
    
    i = 1
    flip = 0
    flag =  True
    while i <= n:
        if (flip % 2 == 0 and a[-i] != b[-i]) or (flip % 2  and a[-i] == b[-i]):
            if (n - i + 1)%2:
                flag = False
                break
            elif prefix[-i]*2 == n-i+1:
                flip += 1
            else:
                flag = False
                break
        i+=1
    if flag:
        print("YES")
    else:
        print("NO")
        
