# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    # Write your code here
    maxs = max(arr)
    freq = [0] * 100
    for i in arr:
        freq[i] += 1
    return freq