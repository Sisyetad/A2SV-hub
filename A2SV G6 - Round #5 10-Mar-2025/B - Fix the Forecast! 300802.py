# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    indexed_a = sorted(enumerate(a), key=lambda x: x[1])
    b.sort()
    result = [0] * n
    for (index, _), b_value in zip(indexed_a, b):
        result[index] = b_value
    print(*result)