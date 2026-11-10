class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Store all start times
        starts = sorted(interval.start for interval in intervals)

        # Store all end times
        ends = sorted(interval.end for interval in intervals)

        start_ptr = 0
        end_ptr = 0

        rooms = 0 
        max_rooms = 0

        while start_ptr < len(intervals):

            # New meeting starts before earliest meeting ends
            if starts[start_ptr] < ends[end_ptr]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)

                start_ptr += 1

            else:
                # A meeting ended, so one room becomes free
                rooms -= 1
                end_ptr += 1

        return max_rooms