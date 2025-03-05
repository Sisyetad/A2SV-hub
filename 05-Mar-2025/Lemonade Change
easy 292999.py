# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5, count10 = 0, 0
        n = len(bills) 
        for i in range(n):
            if bills[i] == 5:
                count5 += 1
                continue
            elif bills[i] == 10:
                if count5:
                    count5 -= 1
                    count10 += 1
                else:
                    return False
            else:
                if count10 and count5:
                    count10 -= 1
                    count5 -= 1
                elif count5 > 2:
                    count5 -= 3
                else:
                    return False
        return True