import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Sort meetings by their start times
        intervals.sort(key=lambda x: x.start)
        
        # Min-heap to store the end times of active meetings
        meeting_rooms = []
        
        # Add the first meeting's end time
        heapq.heappush(meeting_rooms, intervals[0].end)
        
        for meeting in intervals[1:]:
            # If the room with the earliest end time is free, reuse it
            if meeting.start >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            
            # Allocate a room (either a new one, or the reused one with an updated end time)
            heapq.heappush(meeting_rooms, meeting.end)
            
        # The size of the heap is the total number of rooms required
        return len(meeting_rooms)