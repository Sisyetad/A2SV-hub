# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deq = deque()
        deck.sort()
        result = [0]*n
        for i in range(n):
            deq.append(i)
        
        for i in range(n-1):
            result[deq.popleft()] = deck[i]
            poped = deq.popleft()
            deq.append(poped)
        result[deq[0]] = deck[n-1]
        return result