# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point

def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    pionts = sorted(points, key=lambda x: (x[0], x[1]))
    convex_hull = div_hull(points)
    return convex_hull

def div_hull(points):
    if len(points) == 1:
        return points
    else:
        mid = len(points) // 2
        left = div_hull(points[:mid])
        right = div_hull(points[mid:])
        leftHull = div_hull(left)
        rightHull = div_hull(right)
        
        return combind_hull(leftHull, rightHull)
    
    
def combind_hull(left, right):
    if(len(left) == 1) and (len(right) == 1):
        return [left[0], right[0]]
    else:
        rightmost_left_index = max(range(len(left)), key=lambda i: left[i][0])
        leftmost_right_index = min(range(len(right)), key=lambda i: right[i][0])

        upper_tangent = find_upper_tangent(left, right, rightmost_left_index, leftmost_right_index)
        lower_tangent = find_lower_tangent(left, right, rightmost_left_index, leftmost_right_index)

        combind_hull = []
        upper_right = upper_tangent[1]
        lower_right = lower_tangent[1]
        upper_left = upper_tangent[0]
        lower_left = lower_tangent[0]
        
    return left + right

def find_upper_tangent(left, right, leftmost_index, rightmost_index):
    xlm, ylm = right[leftmost_index]
    xrm, yrm = left[rightmost_index]
    # line = (left[leftmost_index], right[rightmost_index])
    
    if xlm == xrm:
        start_slope = 1  # Avoid division by zero (vertical line)
    else:
        start_slope = {(yrm - ylm) / (xrm - xlm)}

    changed = True
    slope_increased = True
    slope_decreased = True

    while changed:
        changed = False
        while slope_increased:
            slope_increased = False
            rx, ry = right[leftmost_index + 1]
            new_slope = (ry - yrm) / (rx - xrm)
            if new_slope > start_slope:
                start_slope = new_slope
                xlm, ylm = rx, ry
                leftmost_index += 1
                changed = True
                slope_increased = True
        
        while slope_decreased:
            slope_decreased = False
            rlx, rly = left[rightmost_index - 1]
            new_slope = (ylm-rly) / (xlm-rlx)
            if new_slope < start_slope:
                start_slope = new_slope
                xrm, yrm = rlx, rly
                rightmost_index -= 1
                changed = True
                slope_decreased = True

    return (rightmost_index, leftmost_index)

def find_lower_tangent(left, right, left_index, right_index):
    xlm, ylm = right[left_index]
    xrm, yrm = left[right_index]
    # line = (left[right_index], right[left_index])

    if xlm == xrm:
        start_slope = 1  # Avoid division by zero (vertical line)
    else:
        start_slope = {(yrm - ylm) / (xrm - xlm)}

    changed = True
    slope_increased = True
    slope_decreased = True

    while changed:
        changed = False
        while slope_increased:
            slope_increased = False
            rx, ry = right[left_index - 1]
            new_slope = (ry - yrm) / (rx - xrm)
            if new_slope < start_slope:
                start_slope = new_slope
                xlm, ylm = rx, ry
                left_index -= 1
                changed = True
                slope_increased = True

        while slope_decreased:
            slope_decreased = False
            rlx, rly = left[right_index + 1]
            new_slope = (ylm - rly) / (xlm - rlx)
            if new_slope > start_slope:
                start_slope = new_slope
                xrm, yrm = rlx, rly
                right_index += 1
                changed = True
                slope_decreased = True

    return (right_index, left_index)

