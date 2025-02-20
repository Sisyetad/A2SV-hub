# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n = int(input())
arr = [str(i) for i in range(1,1000)]
arr = "".join(arr)
print(arr[n-1])