# Graham's Scan
import math

def distance(p0, p1):
    return math.sqrt((p0[0] -p1[0])**2 +(p0[1] -p1[1])**2)

def direction(p1, p2, p3):
    return (p2[0] -p1[0]) *(p3[1] -p1[1]) -(p2[1] -p1[1]) *(p3[0] -p1[0])

def orientation(p1, p2, p3):
    D = direction(p1, p2, p3)
    if D == 0:
        return 0
    return 1 if D >0 else 2

def graham_scan(points):
    P = points[0]
    for p in points:
        if p[1] < P[1] or (p[1] == P[1] and p[0] < P[0]):
            P = p
    def polar_angle(p):
        return math.atan2(p[1] -P[1], p[0] -P[0])

    points.sort(key=polar_angle)
    unique_points = [P]
    for i in range(1, len(points)):
        if i == 1 or direction(P, points[i-1], points[i]) !=0:
            unique_points.append(points[i])
    stack = [unique_points[0], unique_points[1], unique_points[2]]

    for p in unique_points[3:]:
        while len(stack) >1 and orientation(stack[-2], stack[-1], p) ==2:
            stack.pop()
        stack.append(p)

    return stack

points = [(0, 2), (-1, -1), (0, 0), (1, -1)]
print(graham_scan(points))
