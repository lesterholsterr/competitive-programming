# initial solution
# right idea - solve the maxDistance problem in linear time, then run it 3 times.
# needed to do more math in order to get the maxDistance algorithm
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def getManhattanDistance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        def maxDistance(points):
            p = [points[0][0], points[0][1]]
            ans = [0, 0]  # 2 indices, not a coordinate!
            maxsofar = getManhattanDistance(
                points[ans[0]][0], points[ans[0]][1], points[ans[1]][0], points[ans[1]][1])

            # <-- Problem: This does not always find the max distance
            for i in range(1, len(points)):
                x, y = points[i][0], points[i][1]
                if getManhattanDistance(x, y, points[ans[0]][0], points[ans[0]][1]) > maxsofar:
                    # then the new max is with (x, y) and ans[0]
                    ans[1] = i
                elif getManhattanDistance(x, y, points[ans[1]][0], points[ans[1]][1]) > maxsofar:
                    # then the new max is with (x, y) and ans[1]
                    ans[0] = i
                maxsofar = getManhattanDistance(
                    points[ans[0]][0], points[ans[0]][1], points[ans[1]][0], points[ans[1]][1])

            return ans

        i1, i2 = maxDistance(points)
        points1 = points[:i1] + points[i1+1:]
        points2 = points[:i2] + points[i2+1:]
        i3, i4 = maxDistance(points1)
        i5, i6 = maxDistance(points2)
        print(i1, i2, i3, i4, i5, i6)
        return min(getManhattanDistance(points1[i3][0], points1[i3][1], points1[i4][0], points1[i4][1]),
                   getManhattanDistance(points2[i5][0], points2[i5][1], points2[i6][0], points2[i6][1]))

# working solution
# O(n) time, O(1) space
# credit https://leetcode.com/problems/minimize-manhattan-distances/solutions/4949614/c-java-python-sums-and-differences-time-o-n-space-o-1/
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def manhattan(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        def maxDistance(ignore):
            maxS, maxSIndex = -inf, None
            minS, minSIndex = inf, None
            maxD, maxDIndex = -inf, None
            minD, minDIndex = inf, None

            for i in range(len(points)):
                if i == ignore:
                    continue
                
                s = points[i][0] + points[i][1]
                d = points[i][0] - points[i][1]
                if s > maxS:
                    maxS = s
                    maxSIndex = i
                if s < minS:
                    minS = s
                    minSIndex = i
                if d > maxD:
                    maxD = d
                    maxDIndex = i
                if d < minD:
                    minD = d
                    minDIndex = i
            
            if maxS - minS > maxD - minD:
                return (maxSIndex, minSIndex)
            return (maxDIndex, minDIndex)
        
        i1, i2 = maxDistance(-1)
        i3, i4 = maxDistance(i1)
        i5, i6 = maxDistance(i2)
        return min(manhattan(points[i3][0], points[i3][1], points[i4][0], points[i4][1]),
                   manhattan(points[i5][0], points[i5][1], points[i6][0], points[i6][1]))