# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def alternating_subsequence(nums):
    n = len(nums)
    current_max = nums[0]
    result_sum = 0
    
    for i in range(1, n):
        if (nums[i] < 0 and current_max > 0) or (nums[i] > 0 and current_max < 0):
            result_sum += current_max
            current_max = nums[i]
        else:
            current_max = max(current_max, nums[i])
    result_sum += current_max
    return result_sum

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    results.append(alternating_subsequence(nums))


for res in results:
    print(res)