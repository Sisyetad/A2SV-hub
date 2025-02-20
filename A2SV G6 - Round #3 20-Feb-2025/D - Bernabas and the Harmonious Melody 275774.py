# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

test = int(input())
for i in range(test):
    n = int(input())
    s = input()
    def helper(n, s):
        left = 0
        right = n - 1
        removed_count = 0
        removed = ''
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif not removed:
                removed = s[left]
                left += 1
                removed_count += 1
            else:
                if removed == s[left]:
                    left += 1
                    removed_count += 1
                elif removed == s[right]:
                    right -= 1
                    removed_count += 1
                else:
                    return -1
        return removed_count

    removed_left = helper(n, s)
    removed_right = helper(n,s[::-1])
    
    if removed_left == -1 and removed_right == -1:
        print(-1)
    elif removed_left == -1:
        print(removed_right)
    elif removed_right == -1:
        print(removed_left)
    else:
        if removed_left < removed_right:
            print(removed_left)
        else:
            print(removed_right)