# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

n, s = map(int, input().split())
if s//n < s/n:
    print(s//n+1)
elif s//n == s/n:
    print(s//n)
