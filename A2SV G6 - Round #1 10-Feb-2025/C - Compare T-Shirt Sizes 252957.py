# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

n=int(input())
for i in range(n):
    t_shirt1,t_shirt2 = map(str,input().split())
    if t_shirt1[-1] > t_shirt2[-1]:
        print("<")
    elif t_shirt1[-1] < t_shirt2[-1]:
        print(">")
    else:
        if t_shirt2[-1] == 'S':
            if len(t_shirt1) > len(t_shirt2):
                print("<")
            elif len(t_shirt1) < len(t_shirt2) :
                print(">")
            else:
                print("=")
        elif t_shirt2[-1] == 'L':
            if len(t_shirt1) > len(t_shirt2):
                print(">")
            elif len(t_shirt1) < len(t_shirt2) :
                print("<")
            else:
                print("=")
        else:
            print("=")