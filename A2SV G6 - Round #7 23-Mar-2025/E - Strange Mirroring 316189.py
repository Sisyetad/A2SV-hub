# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

def find_kth_character(s, k):
    n = len(s)
    flipped = False  
    i = 0  

    while (2**i) * n < k:
        i += 1

    while k > n:
        half = (2**(i - 1)) * n
        if k > half:
            k -= half  
            flipped = not flipped 
        i -= 1
        
    return s[k-1].swapcase() if flipped else s[k-1]

t = int(input())
for _ in range(t):
    s = input()
    q = int(input())
    queries = map(int, input().split())
    result = []
    for k in queries:
        result.append(find_kth_character(s, k))
    print(*result)