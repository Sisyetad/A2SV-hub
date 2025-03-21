# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

class Solution:
    def helper(self, char, n, s):
        if n == 1:
            return 0 if s[0] == char else 1  

        first_half = sum(1 for i in range(n // 2) if s[i] == char)
        second_half = sum(1 for i in range(n // 2, n) if s[i] == char)

        char = chr(ord(char) + 1)  
        
        return min(
            (n // 2 - first_half) + self.helper(char, n // 2, s[n // 2:]), 
            (n // 2 - second_half) + self.helper(char, n // 2, s[:n // 2])   
        )

    def solve(self):
        import sys
        
        input_fn = lambda: sys.stdin.readline().strip() 
        
        t = int(input_fn())
        for _ in range(t):
            n = int(input_fn())
            s = input_fn()
            print(self.helper('a',n,s))

solution = Solution()
solution.solve()
