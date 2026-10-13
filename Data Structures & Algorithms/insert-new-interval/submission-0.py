class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                i += 1
            else:
                break

        intervals.insert(i, newInterval)
        while i < len(intervals) - 1 and intervals[i+1][1] >= intervals[i][0] and intervals[i][1] >= intervals[i+1][0]:
            new_int = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
            intervals.pop(i)
            intervals[i] = new_int

        return intervals



        
