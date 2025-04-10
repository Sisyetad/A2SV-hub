# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    time = list(map(int, input().split()))
    
    def isvalid(mid, arr, time, k):
        for i in range(len(arr)):
            if arr[i] % mid:
                t = arr[i] // mid + 1
                k -= (time[i] * t)
            else:
                t = arr[i] // mid
                k -= (time[i] * t )  
            
        return k >= 0
    
    def binary_search(start, end, arr, time, k):  
        ans = -1
        while start <= end:
            mid = start + (end - start)//2
            if isvalid(mid, arr, time, k):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
    print(binary_search(1, sum(arr), arr, time, k))