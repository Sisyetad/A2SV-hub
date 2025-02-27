# Problem: C - Restoring to the Original - https://codeforces.com/gym/589822/problem/C

t = int(input())
s = input()
z = s.count("z")
n = s.count("n")
array = []
for i in range( n):
    array.append(1)
for i in range(z):
    array .append(0)
array.sort
print(*array)
