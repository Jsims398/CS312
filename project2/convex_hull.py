# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point



def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    points = sorted(points, key=lambda x: (x[0], x[1]))
    convex_hull = div_hull(points)
    # draw_hull(convex_hull)
    return convex_hull

def div_hull(points):
    points
    if len(points) <= 2:
        return points
    else:
        mid = len(points) // 2
        left = points[:mid]
        right = points[mid:]
        rightHull = div_hull(right)
        leftHull = div_hull(left)
        
        
        return combine_hull(leftHull, rightHull)
    
    
def combine_hull(left, right):
    if (len(left) == 1) and (len(right) == 1):
        return [left[0], right[0]]
    else:
        rightmost_left_index = max(range(len(left)), key=lambda i: left[i][0])
        leftmost_right_index = min(range(len(right)), key=lambda i: right[i][0])

        upper_tangent = find_upper_tangent(left, right, rightmost_left_index, leftmost_right_index)
        lower_tangent = find_lower_tangent(left, right, rightmost_left_index, leftmost_right_index)

        upper_right = upper_tangent[1]
        lower_right = lower_tangent[1]
        upper_left = upper_tangent[0]
        lower_left = lower_tangent[0]
        
        combined_hull = []
        currentPoint = upper_left
        combined_hull.append(left[currentPoint])
        
        # while currentPoint != upper_left:
        #     currentPoint = (currentPoint + 1) % len(left)
        #     combined_hull.append(left[currentPoint])

        currentPoint = upper_right
        combined_hull.append(right[currentPoint])
        while currentPoint != lower_right:
            currentPoint = (currentPoint + 1) % len(right)
            combined_hull.append(right[currentPoint])

        if upper_left != lower_left:
            currentPoint = (lower_left) % len(left)
            # combined_hull.append(left[currentPoint])
            while currentPoint != upper_left:
                combined_hull.append(left[currentPoint])
                currentPoint = (currentPoint + 1) % len(left) 
        return combined_hull

def find_upper_tangent(left, right, left_index, right_index):
    xl, yl = left[left_index]
    xr, yr = right[right_index]

    if xl == xr:
        start_slope = float('inf')  # Avoid division by zero (vertical line)
    else:
        start_slope = (yr - yl) / (xr - xl)

    changed = True
    # left_visited = set()
    # right_visited = set()

    while changed:
        left_visited = set()
        right_visited = set()
        changed = False
        while True:
            left_visited.add(left_index)
            next_left_index = (left_index - 1) % len(left)
            if next_left_index in left_visited:
                break
            left_visited.add(next_left_index)
            lx, ly = left[next_left_index]
            new_slope = (yr - ly) / (xr - lx)
            if new_slope <= start_slope:
                start_slope = new_slope
                xl, yl = lx, ly
                left_index = next_left_index
                changed = True
            else:
                break
        
        # start_slope = (yr - yl) / (xr - xl)
        while True:
            right_visited.add(right_index)
            next_right_index = (right_index + 1) % len(right)
            if next_right_index in right_visited:
                break
            right_visited.add(next_right_index)
            rx, ry = right[next_right_index]
            new_slope = (ry - yl) / (rx - xl)
            if new_slope >= start_slope:
                start_slope = new_slope
                xr, yr = rx, ry
                right_index = next_right_index
                changed = True
            else:
                break
    return left_index, right_index


def find_lower_tangent(left, right, left_index, right_index):
    xl, yl = left[left_index]
    xr, yr = right[right_index]

    if xl == xr:
        start_slope = float('-inf')  # Avoid division by zero (vertical line)
    else:
        start_slope = (yr - yl) / (xr - xl)

    changed = True
    # left_visited = set()
    # right_visited = set()

    while changed:
        left_visited = set()
        right_visited = set()
        changed = False
        while True:
            left_visited.add(left_index)
            next_left_index = (left_index + 1) % len(left)
            if next_left_index in left_visited:
                break
            left_visited.add(next_left_index)
            lx, ly = left[next_left_index]
            new_slope = (yr - ly) / (xr - lx)
            if new_slope >= start_slope:
                start_slope = new_slope
                xl, yl = lx, ly
                left_index = next_left_index
                changed = True
            else:
                break

        while True:
            right_visited.add(right_index)
            next_right_index = (right_index - 1) % len(right)
            if next_right_index in right_visited:
                break
            right_visited.add(next_right_index)
            rx, ry = right[next_right_index]
            new_slope = (ry - yl) / (rx - xl)
            if new_slope <= start_slope:
                start_slope = new_slope
                xr, yr = rx, ry
                right_index = next_right_index
                changed = True
            else:
                break

    return left_index, right_index



# points = [(1, 2), (4, 5), (6, 1), (7, 8), (2, 4), (5, 7), (8, 3), (4, 6), (9, 0), (0, 9)]
# print(compute_hull(points))