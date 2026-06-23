from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        x,y = point
        total = 0

        for (px,py), diagonalcount in self.points.items():
            if abs(px - x) != abs(py-y) or px == x or py == y:
                continue
            corner1count = self.points.get((x,py),0)
            corner2count = self.points.get((px,y),0)

            total += diagonalcount * corner1count * corner2count
        return total