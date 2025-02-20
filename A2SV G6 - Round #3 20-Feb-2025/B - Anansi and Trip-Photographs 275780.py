# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

test = int(input())
for i in range(test):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    left, right = 0, n
    flag = False
    while (left < n) and (right < 2*n):
        if arr[right] - arr[left] < x:
            print("NO")
            flag = True
            break
        right += 1
        left += 1
    if  not flag:
        print("YES")