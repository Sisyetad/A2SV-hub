# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s):
            left, right = 0, len(s) - 1
            count = 0
            remove = ''
            while left <= right:
                if s[right] != s[left]:
                    remove = s[left]
                    left += 1
                    count += 1
                else:
                    left += 1
                    right -= 1
                if count > 1:
                    return False
            return True
        delete_1 = helper(s)
        delete_2 = helper(s[::-1])
        return delete_1 or delete_2