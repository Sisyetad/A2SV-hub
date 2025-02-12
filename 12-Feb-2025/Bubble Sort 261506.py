# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    # Write your code here
        n = len(a)
        i = 0
        swap = 0
        while i < n:
            Sorted = False
            j = 0
            while j < n-i-1:
                if a[j+1] < a[j]:
                    a[j+1],a[j] = a[j],a[j+1]
                    swap += 1
                    Sorted = True
                j += 1
            if not Sorted:
                print(f"Array is sorted in {swap} swaps.")
                print(f"First Element: {a[0]}")
                print(f"Last Element: {a[-1]}")
                return
            i += 1
        print(f"Array is sorted in {swap} swaps.")
        print(f"First Element: {a[0]}")
        print(f"Last Element: {a[-1]}")