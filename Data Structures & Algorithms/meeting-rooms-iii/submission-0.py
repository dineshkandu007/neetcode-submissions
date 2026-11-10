import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()

        # Available rooms: smallest room number first
        available = list(range(n))
        heapq.heapify(available)

        # Busy rooms: (end_time, room_number)
        busy = []

        # Number of meetings held by each room
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free all rooms that are available by meeting start time
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            # If a room is available
            if available:
                # Get lowest numbered room
                room = heapq.heappop(available)

                # Meeting runs at original time
                heapq.heappush(busy, (end, room))

            else:
                # No room available
                # Get room that becomes free first
                end_time, room = heapq.heappop(busy)

                # Delay meeting but keep same duration
                new_end = end_time + duration

                heapq.heappush(busy, (new_end, room))

            # This room handled one more meeting
            count[room] += 1

        # Return room with highest count
        # Lowest room number wins ties
        return count.index(max(count))