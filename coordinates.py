import math
import copy
from tabulate import tabulate
# A class to represent a point in 2D cartesian plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A utility function to find the distance between two points
def dist2(p1,p2):
    p1 = p1.x,p1.y
    p2 = p2.x,p2.y
    return p1,p2

def bruteCoordinates(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                dist2(P[i],P[j])
    return  dist2(P[i],P[j])

    return min_val
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))

def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])

    return min_val

# A utility function to find the distance between the closest points of strip of given size. 
# All points in strip[] are sorted according to# y coordinate. 
# They all have an upper bound on minimum distance as d.
# Note that this method seems to be a O(n^2) method, but it's a O(n) method as the inner loop runs at most 6 times.
def stripClosest(strip, size, d):

    # Initialize the minimum distance as d
    min_val = d


    # Pick all points one by one and try the next points till the difference between y coordinates is smaller than d.
    # This is a proven fact that this loop runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1

    return min_val

# A recursive function to find the smallest distance. 
# The array P contains all points sorted according to x coordinate
def closestUtil(P, Q, n):

    # If there are 2 or 3 points, then use brute force
    if n <= 3:
        return bruteForce(P, n)

    # Find the middle point
    mid = n // 2
    midPoint = P[mid]

    #keep a copy of left and right branch
    Pl = P[:mid]
    Pr = P[mid:]

    # Consider the vertical line passing through the middle point calculate the smallest distance dl on left of middle point and dr on right side
    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid)

    # Find the smaller of two distances
    d = min(dl, dr)

    # Build an array strip[] that contains points close (closer than d) to the line passing through the middle point
    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])

    stripP.sort(key = lambda point: point.y) #<-- REQUIRED
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripQ, len(stripQ), d))


    # Find the self.closest points in strip.
    # Return the minimum of d and self.closest distance is strip[]
    return min(min_a,min_b)

# The main function that findsthe smallest distance.
# This method mainly uses closestUtil()
def closest(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)

    # Use recursive function closestUtil() to find the smallest distance
    return closestUtil(P, Q, n)

print("Enter number of coordinates")
u = input()
n1 = int(u)
e = int(u)
C = []
while n1>0:
    print('Enter coordinate ie. (x,Y)')
    C.append(input())
    n1=n1-1
s = 0
P = []
while s<e:
    c=str(C[s])
    coordinate =  c[1] + c[3]
    P.append(Point(float(c[1]),float(c[3])))
    s=s+1

n = len(P)
table = [['Coordinates', 'closest pair', 'distance'],[C,bruteCoordinates(P,n),closest(P, n)]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
#print("The smallest distance is",closest(P, n))
