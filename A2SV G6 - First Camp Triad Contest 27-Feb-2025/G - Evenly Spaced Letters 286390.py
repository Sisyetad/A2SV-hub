# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

from collections import Counter
 
t = int(input())
 
for _ in range(t):
    arr = list(input())
    
    count = Counter(arr)
    dup = set()
    single = set()
    
    for char, count in count.items():
        if count == 2:
            dup.add(char)
        else:
            single.add(char)
    
    # print(dup)
    listt = list(dup)
    listt.sort()
    
    result = listt + listt + list(single)
    
    print("".join(result))