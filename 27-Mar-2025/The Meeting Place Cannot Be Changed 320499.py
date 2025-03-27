# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

n = int(input())
s = list(map(int, input().split()))
v = list(map(int, input().split()))

initial = min(s)
end = max(s)
precision = 1e-6

def validate(mid):
    max_time = 0
    for i in range(n):
        max_time = max(max_time, abs(s[i] - mid) / v[i])
    return max_time

def binarySearch(initial, end):
    mid = initial + (end - initial) / 2
    ans = validate(mid)
    while end  >= initial + precision:
        mid = initial + (end - initial) / 2
        right_time = validate(mid + precision)
        left_time = validate(mid - precision)
        if right_time < left_time:
            ans = min(ans, right_time)
            initial = mid
        else:
            ans = min(ans, left_time)
            end = mid
    return ans

print(binarySearch(initial, end))