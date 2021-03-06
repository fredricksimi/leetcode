"""
Leetcode 56: Merge Intervals

Given a collection of intervals, merge all overlapping intervals.
"""


class Solution:
    # O(1) space | time - not sure. Should consider the .sort() ?
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort
        intervals.sort(key=lambda item: item[0])

        i = 0
        # no neeed to check the last array
        while (i + 1) < len(intervals):

            curr_a = intervals[i]
            next_a = intervals[i+1]

            # check for overlap
            if curr_a[1] >= next_a[0]:

                # merge
                # we use max coz of such a case: [[1,4],[2,3]]
                # make the last element of the first array be the furthest(largest value)
                intervals[i][1] = max(curr_a[1], next_a[1])

                # delete the second array
                intervals.pop(i+1)

            else:
                i += 1

        return intervals


"""
Example:

Input:
    [[8,10],[15,18], [1,3],[2,6]]
    [[1,3],[2,6],[8,10],[15,18]]
    [[1,3]]
    []
    [[1,4],[4,5]]
    [[1,4],[2,3]]
Output:
    [[1,6],[8,10],[15,18]]
    [[1,6],[8,10],[15,18]]
    [[1,3]]
    []
    [[1,5]]
    [[1,4]]
"""
