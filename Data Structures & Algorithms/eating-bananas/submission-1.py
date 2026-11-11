import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            speed = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / speed)

            # This speed works
            if hours <= h:
                answer = speed

                # Try a smaller speed
                right = speed - 1

            else:
                # Too slow
                left = speed + 1

        return answer