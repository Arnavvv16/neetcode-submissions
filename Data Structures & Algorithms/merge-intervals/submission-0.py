class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start times
        intervals.sort(key=lambda x: x[0])
        res = []

        for interval in intervals:
            # If res is empty OR current interval does NOT overlap with the last one in res
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # There is an overlap; merge by updating the end time to the max possible value
                res[-1][1] = max(res[-1][1], interval[1])

        return res