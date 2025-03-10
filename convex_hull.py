# Convex Hull
def convex_hull(points):
    points.sort()

    def cross(o, a, b):
        return (a[0] -o[0]) * (b[1] -o[1]) - (a[1] -o[1]) * (b[0] -o[0])

    lower =[]
    for p in points:
        while len(lower) >=2 and cross(lower[-2], lower[-1], p) <=0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

points = [(0, 2), (1, 2), (4, 2), (2, 4), (3, 5)]
hull = convex_hull(points)
print(hull)
