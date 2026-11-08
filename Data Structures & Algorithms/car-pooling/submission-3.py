class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0] * 1001

        # Record passenger changes
        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers

        current = 0

        # Process locations from west to east
        for change in changes:
            current += change

            if current > capacity:
                return False

        return True