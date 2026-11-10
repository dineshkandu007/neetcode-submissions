class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start value
        intervals.sort(key=lambda x: x[0])

        # Store merged intervals
        result = []

        for current in intervals:

            # If result is empty OR no overlap
            if not result or result[-1][1] < current[0]:
                result.append(current)

            else:
                # Overlap exists, extend previous interval's end
                result[-1][1] = max(result[-1][1], current[1])

        return result