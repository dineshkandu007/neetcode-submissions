class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort meetings by start time
        intervals.sort(key=lambda x: x.start)

        # Compare each meeting with the previous one
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            current = intervals[i]

            # Conflict if current starts before previous ends
            if current.start < prev.end:
                return False

        return True