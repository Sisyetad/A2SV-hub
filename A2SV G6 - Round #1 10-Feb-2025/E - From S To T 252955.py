# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
q = int(input())
for i in range(q):
    s = list(input())
    t = list(input())
    p = Counter(list(input()))
    i,j = 0,0
    flag = False
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
            j += 1
        elif p[t[j]] > 0:
            p[t[j]] -= 1
            j += 1
        else:
            print("NO")
            flag = True
            break
            
    if not flag and i == len(s):
        print("YES")
    elif not flag and i < len(s):
        print("NO")