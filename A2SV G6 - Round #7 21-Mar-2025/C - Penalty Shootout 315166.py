# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

# Multiple test cases
t = int(input())
for _ in range(t):
    def helper():
        s = input()
        remainingA = remainingB = 5
        chanceA = scoreA = 0
        chanceB = scoreB = 0    
        for i in range(len(s)):
            if i%2:
                if s[i].isdigit():
                    scoreB += int(s[i])
                else:
                    chanceB += 1
                remainingB -= 1
            else:
                if s[i].isdigit():
                    scoreA += int(s[i])
                else:
                    chanceA += 1
                remainingA -= 1
            if scoreA + chanceA > scoreB + remainingB:
                return i + 1
            elif scoreB + chanceB > scoreA + remainingA:
                return i + 1
        return i + 1
    print(helper())