# List of 4 coordinates
left_coords = [(1, 2), (2, 3)]
right_coords = [(4, 5), (5, 2)]

def find_upper_tangent(left, right, left_index, right_index):
    xlm, ylm = left[left_index]
    xrm, yrm = right[right_index]

    if xlm == xrm:
        start_slope = float('inf')  # Avoid division by zero (vertical line)
    else:
        start_slope = (yrm - ylm) / (xrm - xlm)

    changed = True
    left_visited = set()
    right_visited = set()

    while changed:
        changed = False
        while True:
            left_visited.add(left_index)
            next_left_index = (left_index - 1) % len(left)
            if next_left_index in left_visited:
                break
            left_visited.add(next_left_index)
            lx, ly = left[next_left_index]
            new_slope = (yrm - ly) / (xrm - lx)
            if new_slope <= start_slope:
                start_slope = new_slope
                xlm, ylm = lx, ly
                left_index = next_left_index
                changed = True
            else:
                break

        while True:
            right_visited.add(right_index)
            next_right_index = (right_index + 1) % len(right)
            if next_right_index in right_visited:
                break
            right_visited.add(next_right_index)
            rx, ry = right[next_right_index]
            new_slope = (ry - ylm) / (rx - xlm)
            if new_slope >= start_slope:
                start_slope = new_slope
                xrm, yrm = rx, ry
                right_index = next_right_index
                changed = True
            else:
                break
    return left_index, right_index


def find_lower_tangent(left, right, left_index, right_index):
    xlm, ylm = left[left_index]
    xrm, yrm = right[right_index]

    if xlm == xrm:
        start_slope = float('-inf')  # Avoid division by zero (vertical line)
    else:
        start_slope = (yrm - ylm) / (xrm - xlm)

    changed = True
    left_visited = set()
    right_visited = set()

    while changed:
        changed = False
        while True:
            left_visited.add(left_index)
            next_left_index = (left_index - 1) % len(left)
            if next_left_index in left_visited:
                break
            left_visited.add(next_left_index)
            lx, ly = left[next_left_index]
            new_slope = (yrm - ly) / (xrm - lx)
            if new_slope >= start_slope:
                start_slope = new_slope
                xlm, ylm = lx, ly
                left_index = next_left_index
                changed = True
            else:
                break

        while True:
            right_visited.add(right_index)
            next_right_index = (right_index + 1) % len(right)
            if next_right_index in right_visited:
                break
            right_visited.add(next_right_index)
            rx, ry = right[next_right_index]
            new_slope = (ry - ylm) / (rx - xlm)
            if new_slope <= start_slope:
                start_slope = new_slope
                xrm, yrm = rx, ry
                right_index = next_right_index
                changed = True
            else:
                break

    return left_index, right_index


def find_extreme_x_indices(left_list, right_list):
    rightmost_left_index = max(range(len(left_list)), key=lambda i: left_list[i][0]) if left_list else None
    leftmost_right_index = min(range(len(right_list)), key=lambda i: right_list[i][0]) if right_list else None
    return rightmost_left_index, leftmost_right_index


# Example usage
left_idx, right_idx = find_extreme_x_indices(left_coords, right_coords)

if left_idx is not None and right_idx is not None:
    x1, y1 = left_coords[left_idx]
    x2, y2 = right_coords[right_idx]

    if x1 == x2:
        print("None")  # Avoid division by zero (vertical line)
    else:
        print(f"Slope: {(y2 - y1) / (x2 - x1)}")

    print(f"Rightmost left index: {left_idx}, Coordinate: {left_coords[left_idx]}")
    print(f"Leftmost right index: {right_idx}, Coordinate: {right_coords[right_idx]}")
else:
    print("Invalid input: One of the lists is empty.")

# Fixing the argument order when calling the tangent functions
upper_tangent = find_upper_tangent(left_coords, right_coords, left_idx, right_idx)
lower_tangent = find_lower_tangent(left_coords, right_coords, left_idx, right_idx)

print(f"Upper tangent: {upper_tangent}")
print(f"Lower tangent: {lower_tangent}")

combined_hull = []
upper_right = upper_tangent[1]
lower_right = lower_tangent[1]
upper_left = upper_tangent[0]
lower_left = lower_tangent[0]

print(f"Upper right: {right_coords[upper_right]}, Lower right: {right_coords[lower_right]}, Upper left: {left_coords[upper_left]}, Lower left: {left_coords[lower_left]}")
