class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        rooms = 0
        end_ptr = 0
        
        for start in starts:
            if start < ends[end_ptr]:
                # Need a new room
                rooms += 1
            else:
                # We can reuse the room, move to the next oldest end time
                end_ptr += 1
                
        return rooms