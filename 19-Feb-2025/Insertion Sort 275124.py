# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    val = arr[-1] 
    i = n - 2 
    
    while i >= 0 and arr[i] > val:
        arr[i + 1] = arr[i]  
        print(*arr) 
        i -= 1
    
    arr[i + 1] = val 
    print(*arr)  