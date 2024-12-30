# https://leetcode.com/problems/detect-squares/

# Initial - doesn't seem to detect duplicates, but I don't see what's wrong
from collections import defaultdict

class DetectSquares:
    """
    - initial thought: of the 3 points you choose, 2 must share an x-val. 2 must share a y-val. 
    - so group the points based on x and y values
    - given the 4th point, we consider all pairs of 2 points: 1 sharing x-val, 1 sharing y-val, both same distance
    - for each of these pairs, check if the final point also exists
    """
    def __init__(self):
        self.points_x = [defaultdict(int) for _ in range(1001)]
        self.points_y = [defaultdict(int) for _ in range(1001)]

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points_x[x][(x, y)] += 1
        self.points_y[y][(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        valid_x = self.points_x[x]
        valid_y = self.points_y[y]
        for px, py in valid_x.keys():
            side = abs(y - py)
            if (x + side, y) in valid_y or (x - side, y) in valid_y:
                if (x + side, y + side) in self.points_x[x + side]:
                    res += self.points_x[x + side][(x + side, y + side)]
                if (x - side, y + side) in self.points_x[x - side]:
                    res += self.points_x[x - side][(x - side, y + side)]
                if (x + side, y - side) in self.points_x[x + side]:
                    res += self.points_x[x + side][(x + side, y - side)]
                if (x - side, y - side) in self.points_x[x - side]:
                    res += self.points_x[x - side][(x - side, y - side)]
        return res

# Second try - glanced at solution.
# Realize that the fancy shit I tried with points_x and points_y is worst case the same time as brute force.
# So... just brute force it. A really nice way to check the points is to find DIAGONAL POINTS to the queried one
# and then check whether the other 2 diagonal points exist, and in what quantities.
class DetectSquares:
    def __init__(self):
        self.points = []
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.freq[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for px, py in self.points:
            if abs(x - px) == abs(y - py) and x != px: # <-- diagonal points!
                res += self.freq[(x, py)] * self.freq[(px, y)]
        return res