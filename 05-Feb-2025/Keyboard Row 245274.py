# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dictionary = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        arr = []
        for i in words:
            if not (set(i.lower()) - dictionary[0] and set(i.lower()) - dictionary[1] and set(i.lower()) - dictionary[2]):
                arr.append(i)
        return arr