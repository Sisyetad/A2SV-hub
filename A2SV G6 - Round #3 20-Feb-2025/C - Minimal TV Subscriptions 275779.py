# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
test = int(input())
for i in range(test):
    n, k, d = map(int, input().split())
    arr = list(map(int, input().split()))
    window = 0
    ans = Counter()
    for i in range(d):
        window += arr[i]
        ans[arr[i]] += 1
    left = 0 
    min_show = window
    count = len(ans)
    for right in  range(d, n):
        window += arr[right]
        window -= arr[left]
        ans[arr[right]] += 1
        ans[arr[left]] -= 1
        if ans[arr[left]] == 0:
            del ans[arr[left]]
        left += 1
        if min_show > window or count > len(ans):
            min_show = window
            count = min(count,len(ans))
    print(count)