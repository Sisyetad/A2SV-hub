# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int,input().split()))
ans = []
sum_1 = 0
sum_2 = 0
left = 0
right = 0
while left < n or right < m:
    
    if left <n:
        sum_1 += arr_1[left]
        left += 1
    if right < m:
        sum_2 += arr_2[right]
        right += 1

    while sum_1 != sum_2:
        if sum_1 < sum_2 and left < n:
            sum_1 += arr_1[left]
            left += 1
        elif sum_1 > sum_2 and right < m:
            sum_2 += arr_2[right]
            right += 1         
        else:
            break
    if sum_1 == sum_2:
        ans.append(sum_2)
        sum_1 = 0
        sum_2 = 0

if sum_1 != sum_2:
    print(-1)
else:
    print(len(ans))