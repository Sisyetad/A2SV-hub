# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary1 = {list1[i] : i for i in range(len(list1))}
        dictionary2 = {list2[i] : i for i in range(len(list2))}
        ans = len(list1) + len(list2)
        for i in dictionary1:
            if i in dictionary2:
                if ans > dictionary1[i]+dictionary2[i]:
                    ans = dictionary1[i]+dictionary2[i]
                    item = [i]
                elif ans == dictionary1[i]+dictionary2[i]:
                    item.append(i)
        return item