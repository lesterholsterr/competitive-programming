# https://leetcode.com/problems/meeting-rooms/description/

# Initial - not much to say
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        sort by meeting start. easy linear scan. O(nlogn) time
        can we do it without sorting? Don't think so?
        """
        if len(intervals) <= 1:
            return True
        
        intervals.sort()
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if last_end > intervals[i][0]:
                return False
            last_end = intervals[i][1]
        return True

