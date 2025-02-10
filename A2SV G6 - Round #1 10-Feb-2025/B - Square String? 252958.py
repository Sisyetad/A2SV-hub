# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

n = int(input())
for i in range(n):
    test = input().strip()
    if(len(test)<2):
        print("NO")
    elif test[:(len(test)//2)] == test[len(test)//2:]:
        print("YES")
    else:
        print("NO")