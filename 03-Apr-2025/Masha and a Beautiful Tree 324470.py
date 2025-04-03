# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D


def merge(left_half, right_half):
    if left_half[-1] < right_half[0]:  
        return left_half + right_half, 0
    else:
        return right_half + left_half, 1  

def merge_sort(left, right, arr):
    if right - left == 1: 
        return arr[left:right], 0

    mid = left + (right - left) // 2
    left_half, swaps_left = merge_sort(left, mid, arr)
    right_half, swaps_right = merge_sort(mid, right, arr)

    merged, swap_count = merge(left_half, right_half)
    
    return merged, swaps_left + swaps_right + swap_count

def solve():
    t = int(input()) 
    for _ in range(t):
        m = int(input()) 
        arr = list(map(int,input().split()))

        if arr == sorted(arr):  
            print(0)
            continue

        sorted_arr, swaps = merge_sort(0, m, arr[:])  

        if sorted_arr != sorted(arr): 
            print(-1)
        else:
            print(swaps)


solve()

