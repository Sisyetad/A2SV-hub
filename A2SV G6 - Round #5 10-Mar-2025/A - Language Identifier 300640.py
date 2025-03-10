# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A

t = int(input())
for _ in  range(t):
    s = input()
    if s[-2:] == "po":
        print("FILIPINO")
    elif s[-5:] == "mnida":
        print("KOREAN")
    elif s[-4:] == "desu" or s[-4:] == "masu":
        print("JAPANESE")