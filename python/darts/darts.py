from math import sqrt

class Point:
    """ Defines a basic Point class. """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'P({self.x}, {self.y})'

def distance(p1:Point, p2:Point) -> float:
    """ Calculates the distance between to points P(x1, y1) and P(x2, y2). """
    return sqrt( (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 )


def score(x, y) -> int:
    """ Dart game logic. Returns score based on P(x, y) as input. """

    # Store a pair of (radio, score) per circle.
    circles = ( (1, 10), (5, 5), (10, 1) )

    # Calculate distance of point (x, y) from the origin.
    d = distance( Point(0, 0), Point(x, y) )

    # Check if point P(x, y) hits any of the circles.
    for c in circles:
        if d <= distance( Point(0, 0), Point(0, c[0]) ):
            # If there is a hit then returns the corresponding score.
            return c[1]
    # If there is no hit then return score 0.
    return 0
