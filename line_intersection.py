# Line Intersection
def direction(p1, p2, p3):
    return (p2[0] -p1[0]) *(p3[1] -p1[1]) - (p2[1] - p1[1]) *(p3[0] - p1[0])

def on_segment(p, q, r):
    return min(p[0], r[0]) <=q[0] <= max(p[0],r[0]) and min(p[1], r[1]) <=q[1] <= max(p[1],r[1])

def orientation(p, q, r):
    val = direction(p, q, r)
    if val == 0:
        return 0
    elif val >0:
        return 1
    else:
        return 2

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 !=o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

p1 = (1, 1)
q1 = (10, 1)
p2 = (1, 2)
q2 = (10, 2)

print(do_intersect(p1, q1, p2, q2))
