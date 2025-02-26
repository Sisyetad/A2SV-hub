# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    ans = [
        max(0, max(b, c) - a + 1),
        max(0, max(a, c) - b + 1),
        max(0, max(a, b) - c + 1)
    ]
    
    print(*ans)
