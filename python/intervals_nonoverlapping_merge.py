"""
Problem Description
You have a set of non-overlapping intervals. You are given a new interval [start, end], insert this new interval into the set of intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Problem Constraints
0 <= |intervals| <= 105



Input Format
First argument is the vector of intervals

second argument is the new interval to be merged



Output Format
Return the vector of intervals after merging



Example Input
Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output
Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]


Example Explanation
Explanation 1:

(2,5) does not completely merge the given intervals
Explanation 2:

(2,6) completely merges the given intervals

"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self) -> str:
        return f"[{self.start}, {self.end}]"
    
    def __eq__(self, othr: object) -> bool:
        return othr.start == self.start and othr.end == self.end

def solve(intervals, newInterval):
    i=0
    ans= []
    while i < len(intervals):
        currInterval = intervals[i]
        if newInterval.end < currInterval.start: # newInterval is left and out
            ans.append(newInterval)
            while i < len(intervals): # add remaining intervals
                ans.append(intervals[i])
                i+=1
            return ans
        elif newInterval.start > currInterval.end: # # newInterval is right and out
            ans.append(currInterval)
            i+=1
            continue
        else: # currInterval and newInterval overlaps
            newInterval.start = min (newInterval.start, currInterval.start)
            newInterval.end = max(newInterval.end, currInterval.end)
            i+=1
     
    ans.append(newInterval)
    # print(ans)
    return ans

        


def c1(l): # convert_to_interval
   return Interval(l[0], l[1])

def c2(l): # convert_list_to_intervals
    return [c1(x) for x in l]
        


print(solve(c2([[1, 3], [6, 9]]), c1([2, 5])) == c2([ [1, 5], [6, 9] ])) # 
print(solve(c2([[1, 3], [6, 9] ]), c1([2, 6])) == c2([ [1, 9] ])) 