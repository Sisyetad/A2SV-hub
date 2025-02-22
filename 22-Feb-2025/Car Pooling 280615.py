# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for numPassengers, start, end in trips:
            events.append((start, numPassengers))  # Pick up event
            events.append((end, -numPassengers))   # Drop off event

        events.sort()  # Sort by location

        current_passengers = 0
        for _, passengers in events:
            current_passengers += passengers
            if current_passengers > capacity:
                return False

        return True
